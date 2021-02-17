import unittest


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class FirstTest(unittest.TestCase):
    def test(self):
        self.driver = webdriver.Chrome(r"C:\Users\vin\PycharmProjects\seleniumTest01\Browsers\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.google.com")

    def test_search_keyword(self):
        self.driver.find_element_by_name("q").send_keys("myntra")
        print("search for the element")
        time.sleep(5)
        self.driver.find_element_by_class_name("gNO89b").send_keys(Keys.ENTER)
        self.driver.close()

