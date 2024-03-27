from selenium.webdriver.common.by import By


class HomePage:
    lnk_my_account_xpath = "//a[@title='My Account']"
    lnk_register_link_text = "Register"
    lnk_login_link_text = "Login"

    def __init__(self, driver):
        self.driver = driver

    # Action methods
    def click_my_account(self):
        self.driver.find_element(By.XPATH, self.lnk_my_account_xpath).click()

    def click_register(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_register_link_text).click()

    def click_login(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_login_link_text).click()
