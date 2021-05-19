import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CheckOutPage import CheckOutPage
from PageObjects.ConfirmPage import ConfirmPage
from PageObjects.HomePage import HomePage
from TestData.E2ETestdata import E2ETestdata
from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass

#@pytest.mark.usefixtures("setup")


class Testone(BaseClass):
    def test_e2e(self, getData):

        log = self.getlogger()
        # Putting Objects into PageObjects package and retriving from that location
        homepage = HomePage(self.driver)
        # self.driver.find_element_by_xpath("//a[contains(text(), 'Shop')]").click()
        checkoutpage = homepage.shop_items()
        log.info(checkoutpage)

        # products = self.driver.find_elements_by_xpath("//div[@class = 'card h-100']")
        # checkoutpage = CheckOutPage(self.driver)
        products = checkoutpage.getCardTitles()

        i = -1
        for product in products:
            i = i + 1
            productname = product.text
            if productname == "Blackberry":
                checkoutpage.getCardFooter().click()

        # self.driver.find_element_by_xpath("//a[contains(text(), 'Checkout')]").click()
        checkoutpage.getcheckout().click()
        log.info("Checkout has been initiated")
        # products_in_cart = self.driver.find_elements_by_xpath("media-heading")
        checkoutpage.getproducts_from_cart()

        # assert productName == products_in_cart

        # self.driver.find_element_by_xpath("//button[contains(text(), 'Checkout' )]").click()
        confirmpage = checkoutpage.getcheckoutbutton()

        # confirmpage = ConfirmPage(self.driver)
        # self.driver.find_element_by_id("country").send_keys("ind")
        confirmpage.set_country_code().send_keys(getData["Country"])
        log.info("Sending country as : IND")

        # wait = WebDriverWait(self.driver, 7)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India')))
        self.verify_presence('India')

        # self.driver.find_element_by_link_text("India").click()
        confirmpage.set_country_selection().click()

        # self.driver.find_element_by_xpath("//div[@class = 'checkbox checkbox-primary']").click()
        confirmpage.set_terms_condition().click()

        # self.driver.find_element_by_css_selector("input[value = 'Purchase']").click()
        confirmpage.set_purchasable().click()

        success_msg = self.driver.find_element_by_class_name("alert-success").text
        log.info(success_msg)

        assert "Success! Thank you!" in success_msg

        # self.driver.get_screenshot_as_file("success.png")
        self.screen_capture()

    @pytest.fixture(params=E2ETestdata.e2e_test_data)
    def getData(self, request):
        return request.param

