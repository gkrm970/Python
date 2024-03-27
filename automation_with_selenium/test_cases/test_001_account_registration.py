import os.path
import string

from page_objects.home_page import HomePage
from page_objects.account_registration_page import AccountRegistrationPage
from utilities.custom_logger import logger
from utilities.random_string import random_string_generator
from utilities.read_properties import ReadConfig


class Test001AccountRegistration:
    base_url = ReadConfig.get_application_url()

    def test_account_reg(self, setup):
        logger.info("**** Test_001_Account_Registration ****")
        self.driver = setup
        self.driver.get(self.base_url)
        logger.info("**** Navigated to Home Page ****")
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        logger.info("**** Click on My Account ****")
        self.hp.click_my_account()
        self.hp.click_register()
        logger.info("**** Click on Register ****")
        self.regpage = AccountRegistrationPage(self.driver)

        self.regpage.set_first_name("Vijay")
        self.regpage.set_last_name("Kumar")
        # self.regpage.txt_email_name("abc@gmail.com")
        # create the random email id
        self.gmail_com_ = (
            random_string_generator(
                size=5, chars=string.ascii_lowercase + string.digits
            )
            + "@gmail.com"
        )
        self.regpage.set_email(self.gmail_com_)
        self.regpage.set_telephone("65656565")
        self.regpage.set_password("abcxyz")
        self.regpage.set_confirm_password("abcxyz")
        self.regpage.set_privacy_policy()
        self.regpage.click_continue()
        self.confmsg = self.regpage.get_confirmation_msg()
        self.driver.close()
        if self.confmsg == "Your Account Has Been Created!":
            logger.info("**** Account Created Successfully ****")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screen_shorts\\test_account_reg.png")
            self.driver.close()
            assert False

        logger.info("**** Test_001_Account_Registration Completed ****")
