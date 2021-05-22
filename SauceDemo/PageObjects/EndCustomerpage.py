from selenium.webdriver.common.by import By

from Utilities.BaseClass import BaseClass


class EndCustomerPage(BaseClass):

    f_name = (By.CSS_SELECTOR, "#first-name")
    l_name = (By.CSS_SELECTOR, "#last-name")
    postal_code = (By.CSS_SELECTOR, "#postal-code")
    continue_to_checkout = (By.CSS_SELECTOR, "#continue")
    final_placement = (By.CSS_SELECTOR, "#finish")
    success_header = (By.CSS_SELECTOR, "h2[class = 'complete-header']")

    def __init__(self, driver):
        self.driver = driver

    def get_fname(self):
        return self.driver.find_element(*EndCustomerPage.f_name)

    def get_lname(self):
        return self.driver.find_element(*EndCustomerPage.l_name)

    def get_postal_code(self):
        return self.driver.find_element(*EndCustomerPage.postal_code)

    def get_final_checkout(self):
        return self.driver.find_element(*EndCustomerPage.continue_to_checkout)

    def get_final_placement(self):
        return self.driver.find_element(*EndCustomerPage.final_placement)

    def get_header_text(self):
        return self.driver.find_element(*EndCustomerPage.success_header)
