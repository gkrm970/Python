import time
from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage
from page_objects.my_account_page import MyAccountPage
from utilities import xl_utils
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
import os


class Test_Login_DDT():
    base_url = ReadConfig.get_application_url()
    logger = LogGen.loggen()  # Logger

    path = os.path.abspath(os.curdir) + "\\testdata\\Opencart_LoginData.xlsx"

    def test_login_ddt(self, setup):
        self.logger.info("**** Starting test_003_login_Datadriven *******")
        self.rows = xl_utils.get_row_count(self.path, 'Sheet1')
        lst_status = []

        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)  # HomePage Page Object Class
        self.lp = LoginPage(self.driver)  # LoginPage Page Object Class
        self.ma = MyAccountPage(self.driver)  # MyAccount Page Object class

        for r in range(2, self.rows + 1):
            self.hp.click_my_account()
            self.hp.click_login()

            self.email = xl_utils.read_data(self.path, "Sheet1", r, 1)
            self.password = xl_utils.read_data(self.path, "Sheet1", r, 2)
            self.exp = xl_utils.read_data(self.path, "Sheet1", r, 3)
            self.lp.set_email(self.email)
            self.lp.set_password(self.password)
            self.lp.click_login()
            time.sleep(3)
            self.target_page = self.lp.is_my_account_page_exists()

            if self.exp == 'Valid':
                if self.target_page:
                    lst_status.append('Pass')
                    self.ma.click_logout()
                else:
                    lst_status.append('Fail')
            elif self.exp == 'Invalid':
                if self.target_page:
                    lst_status.append('Fail')
                    self.ma.click_logout()
                else:
                    lst_status.append('Pass')
        self.driver.close()
        # final validation
        if "Fail" not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("******* End of test_003_login_Datadriven **********")
