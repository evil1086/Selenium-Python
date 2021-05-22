from selenium.webdriver.common.by import By

from Utilities.BaseClass import BaseClass


class CheckOut(BaseClass):

    cart_link = (By.CSS_SELECTOR, "a[class = 'shopping_cart_link']")
    checkout_button = (By.CSS_SELECTOR, "#checkout")

    def __init__(self, driver):
        self.driver = driver

    def get_cart_link(self):
        return self.driver.find_element(*CheckOut.cart_link)

    def set_checkout(self):
        return self.driver.find_element(*CheckOut.checkout_button)
