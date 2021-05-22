from PageObjects.LoginPage import Loginpage
from PageObjects.MarketplacePage import Marketplace
from PageObjects.CheckoutPage import CheckOut
from PageObjects.EndCustomerpage import EndCustomerPage
from Utilities.BaseClass import BaseClass


class Testsauce(BaseClass):

    def test_loginpage(self):

        log = self.getlogger()

        loginpage = Loginpage(self.driver)
        # driver.find_element_by_css_selector("#user-name").send_keys("standard_user")
        loginpage.set_username().send_keys("standard_user")
        # driver.find_element_by_css_selector("#password").send_keys("secret_sauce")
        loginpage.set_pass_word().send_keys("secret_sauce")
        # driver.find_element_by_css_selector("input[name = 'login-button']").click()
        loginpage.set_login_button().click()
        log.info("Login successful")

        marketplace_page = Marketplace(self.driver)
        # adding all the products into the cart
        # list_of_products = driver.find_elements_by_xpath("//div[@class = 'inventory_item']/div[@class = 'inventory_item_description']"
        #                                              "/div[@class = 'pricebar']/button")
        list_of_products = marketplace_page.add_to_cart()

        for product in list_of_products:
            if product.text == "Add to cart":
                product.click()

        log.info("Items added to the cart")

        checkout = CheckOut(self.driver)

        # driver.find_element_by_css_selector("a[class = 'shopping_cart_link']").click()
        checkout.get_cart_link().click()
        # driver.find_element_by_css_selector("#checkout").click()
        checkout.set_checkout().click()
        log.info("Checkout has been done")

        end_customer = EndCustomerPage(self.driver)
        # driver.find_element_by_css_selector("#first-name").send_keys("Vinod")
        end_customer.get_fname().send_keys("Vinod")

        # driver.find_element_by_css_selector("#last-name").send_keys("Pawar")
        end_customer.get_lname().send_keys("Pawar")

        # driver.find_element_by_css_selector("#postal-code").send_keys("410502")
        end_customer.get_postal_code().send_keys("410502")
        log.info("End Customers details had been added")

        # driver.find_element_by_css_selector("#continue").click()
        end_customer.get_final_checkout().click()

        # driver.find_element_by_css_selector("#finish").click()
        end_customer.get_final_placement().click()

        # confirm_text = driver.find_element_by_css_selector("h2[class = 'complete-header']").text
        confirm_text = end_customer.get_header_text().text

        assert "THANK " in confirm_text
        log.info("")

        self.screen_capture()

