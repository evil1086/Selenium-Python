from selenium.webdriver.common.by import By

from Utilities.BaseClass import BaseClass


class Marketplace(BaseClass):

    items = (By.XPATH, "//div[@class = 'inventory_item']/div[@class = 'inventory_item_description']"
                                                     "/div[@class = 'pricebar']/button")

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        return self.driver.find_elements(*Marketplace.items)
