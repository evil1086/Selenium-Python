from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    # driver.find_elements_by_xpath("//div[@class = 'card h-100']")
    card_title = (By.XPATH, "//div[@class = 'card h-100']")
    card_footer = (By.XPATH, "//div[@class = 'card h-100'")
    # driver.find_element_by_xpath("//a[contains(text(), 'Checkout')]")
    checkout = (By.XPATH, "//a[contains(text(), 'Checkout')]")
    # self.driver.find_elements_by_xpath("media-heading")
    checkout_products_in_cart = (By.XPATH, "media-heading")
    # driver.find_element_by_xpath("//button[contains(text(), 'Checkout' )]")
    checkout_button = (By.XPATH, "//button[contains(text(), 'Checkout' )]")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.card_title)

    def getCardFooter(self):
        return self.driver.find_element(*CheckOutPage.card_footer)

    def getcheckout(self):
        return self.driver.find_element(*CheckOutPage.checkout)

    def getproducts_from_cart(self):
        return self.driver.find_elements(*CheckOutPage.checkout_products_in_cart)

    def getcheckoutbutton(self):
        self.driver.find_element(*CheckOutPage.checkout_button).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage








