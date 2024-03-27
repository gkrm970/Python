from selenium.webdriver.common.by import By


class AccountRegistrationPage:
    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    txt_email_name = "email"
    txt_telephone_name = "telephone"
    txt_password_name = "password"
    txt_confirm_password_name = "confirm"
    chk_policy_name = "agree"
    btn_cont_xpath = "//input[@value='Continue']"
    text_msg_conf_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self, driver):
        self.driver = driver

    def set_first_name(self, fname):
        self.driver.find_element(By.NAME, self.txt_firstname_name).send_keys(fname)

    def set_last_name(self, lname):
        self.driver.find_element(By.NAME, self.txt_lastname_name).send_keys(lname)

    def set_email(self, email):
        self.driver.find_element(By.NAME, self.txt_email_name).send_keys(email)

    def set_telephone(self, tel):
        self.driver.find_element(By.NAME, self.txt_telephone_name).send_keys(tel)

    def set_password(self, pwd):
        self.driver.find_element(By.NAME, self.txt_password_name).send_keys(pwd)

    def set_confirm_password(self, cnfpwd):
        self.driver.find_element(By.NAME, self.txt_confirm_password_name).send_keys(
            cnfpwd
        )

    def set_privacy_policy(self):
        self.driver.find_element(By.NAME, self.chk_policy_name).click()

    def click_continue(self):
        self.driver.find_element(By.XPATH, self.btn_cont_xpath).click()

    def get_confirmation_msg(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_msg_conf_xpath).text
        except:
            return None
