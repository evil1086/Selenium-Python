from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    # driver.find_element_by_id("country")
    country_selection = (By.ID, "country")
    # driver.find_element_by_link_text("India")
    confirm_country = (By.LINK_TEXT, "India")
    # driver.find_element_by_xpath("//div[@class = 'checkbox checkbox-primary']")
    terms_condition = (By.XPATH, "//div[@class = 'checkbox checkbox-primary']")
    # driver.find_element_by_css_selector("input[value = 'Purchase']")
    purchase = (By.CSS_SELECTOR, "input[value = 'Purchase']")

    def set_country_code(self):
        return self.driver.find_element(*ConfirmPage.country_selection)

    def set_country_selection(self):
        return self.driver.find_element(*ConfirmPage.confirm_country)

    def set_terms_condition(self):
        return self.driver.find_element(*ConfirmPage.terms_condition)

    def set_purchasable(self):
        return self.driver.find_element(*ConfirmPage.purchase)
