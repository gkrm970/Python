import pytest

from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import logger
import os


class Test_Login:
    baseURL = ReadConfig.get_application_url()

    user = ReadConfig.get_user_email()
    password = ReadConfig.get_password()

    @pytest.mark.regression
    def test_login(self, setup):
        logger.info("******* Starting test_002_login **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.click_my_account()
        self.hp.click_login()

        self.lp = LoginPage(self.driver)
        self.lp.set_email(self.user)
        self.lp.set_password(self.password)
        self.lp.click_login()

        self.target_page = self.lp.is_my_account_page_exists()
        if self.target_page:
            assert True
        else:
            self.driver.save_screenshot(
                os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login"
            )
            assert False

        self.driver.close()
        logger.info("******* End of test_002_login **********")
