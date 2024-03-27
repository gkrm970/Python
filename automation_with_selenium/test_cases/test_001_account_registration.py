import os.path
import string

from page_objects.home_page import HomePage
from page_objects.account_registration_page import AccountRegistrationPage
from utilities.random_string import random_string_generator


class Test001AccountRegistration:
    base_url = "https://demo.opencart.com/"

    def test_account_reg(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.click_my_account()
        self.hp.click_register()
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
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath("../screenshots/test_account_reg.png"))
            self.driver.close()
            assert False
