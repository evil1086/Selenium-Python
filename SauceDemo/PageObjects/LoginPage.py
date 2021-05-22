from selenium.webdriver.common.by import By

from Utilities.BaseClass import BaseClass


class Loginpage(BaseClass):

    user_name = (By.CSS_SELECTOR, "#user-name")
    pass_word = (By.CSS_SELECTOR, "#password")
    login_button = (By.CSS_SELECTOR, "input[name = 'login-button']")

    def __init__(self, driver):
        self.driver = driver

    def set_username(self):
        return self.driver.find_element(*Loginpage.user_name)

    def set_pass_word(self):
        return self.driver.find_element(*Loginpage.pass_word)

    def set_login_button(self):
        return self.driver.find_element(*Loginpage.login_button)


