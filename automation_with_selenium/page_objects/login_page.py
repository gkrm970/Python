from selenium.webdriver.common.by import By


class LoginPage:
    txt_email_xpath = "//input[@id='input-email']"
    txt_password_xpath = "//input[@id='input-password']"
    btn_login_xpath = "//input[@value='Login']"
    msg_my_account_xpath = "//h2[text()='My Account']"

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def set_password(self, pwd):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(pwd)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def is_my_account_page_exists(self):
        try:
            return self.driver.find_element(
                By.XPATH, self.msg_my_account_xpath
            ).is_displayed()
        except:
            return False
