import pytest
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass


class Testhome(BaseClass):
    def test_home(self, getData):
        homepage = HomePage(self.driver)
        # driver.find_element_by_css_selector("input[name='name']").send_keys("Vinod Pawar")
        homepage.set_name().send_keys(getData["FirstName"])
        # driver.find_element_by_css_selector("input[name='email']").send_keys("VinodPawar@maildrop.cc")
        homepage.set_email().send_keys(getData["E-mail"])
        # driver.find_element_by_css_selector("#exampleInputPassword1").send_keys("vinodpawar")
        homepage.set_password().send_keys(getData["LastName"])
        # driver.find_element_by_css_selector("#exampleCheck1").click()
        homepage.set_check_boxes().click()

        # dropdown = Select(homepage.set_dropdown())
        # dropdown.select_by_visible_text("Male")
        self.selectdropdown(homepage.set_dropdown(), getData["Gender"])

        # driver.find_element_by_css_selector("#inlineRadio2").click()
        homepage.set_password().click()
        # driver.find_element_by_css_selector("input[name='bday']").send_keys("09091995")
        homepage.set_DOB().send_keys(getData["DOB"])
        # driver.find_element_by_css_selector("input[value='Submit']").click()
        homepage.set_submit().click()
        # text = self.driver.find_element_by_css_selector("[class*= 'alert-success']").text
        text = homepage.get_text().text

        assert ("Success" in text)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.get_testdata("TestCase1"))
    def getData(self, request):
        return request.param


