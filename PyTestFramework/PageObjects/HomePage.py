from selenium.webdriver.common.by import By



from PageObjects.CheckOutPage import CheckOutPage


class HomePage:

    shop = (By.XPATH, "//a[contains(text(), 'Shop')]")
    # driver.find_element_by_css_selector("input[name='name']").send_keys("Vinod Pawar")
    name = (By.CSS_SELECTOR, "input[name='name']")
    # driver.find_element_by_css_selector("input[name='email']").send_keys("VinodPawar@maildrop.cc")
    email  = (By.CSS_SELECTOR, "input[name='email']")
    # driver.find_element_by_css_selector("#exampleInputPassword1").send_keys("vinodpawar")
    password = (By.CSS_SELECTOR, "#exampleInputPassword1")
    # driver.find_element_by_css_selector("#inlineRadio2").click()
    radio_button = (By.CSS_SELECTOR, "#inlineRadio2")
    # driver.find_element_by_css_selector("#exampleCheck1").click()
    check_boxes = (By.CSS_SELECTOR, "#exampleCheck1")
    # driver.find_element_by_css_selector("input[name='bday']").send_keys("09091995")
    date_choooser = (By.CSS_SELECTOR, "input[name='bday']")
    # driver.find_element_by_css_selector("input[value='Submit']").click()
    subbutton = (By.CSS_SELECTOR, "input[value='Submit']")
    # self.driver.find_element_by_css_selector("[class*= 'alert-success']")
    text_get = (By.CSS_SELECTOR, "[class*= 'alert-success']")
    # self.driver.find_element_by_css_selector("#exampleFormControlSelect1")
    dropdown = (By.CSS_SELECTOR, "#exampleFormControlSelect1")

    def __init__(self, driver):
        self.driver = driver

    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage

    def set_name(self):
        return self.driver.find_element(*HomePage.name)

    def set_email(self):
        return self.driver.find_element(*HomePage.email)

    def set_password(self):
        return self.driver.find_element(*HomePage.password)

    def set_radio_bbutton(self):
        return self.driver.find_element(*HomePage.radio_button)

    def set_check_boxes(self):
        return self.driver.find_element(*HomePage.check_boxes)

    def set_DOB(self):
        return self.driver.find_element(*HomePage.date_choooser)

    def set_submit(self):
        return self.driver.find_element(*HomePage.subbutton)

    def get_text(self):
        return self.driver.find_element(*HomePage.text_get)

    def set_dropdown(self):
        return self.driver.find_element(*HomePage.dropdown)




        #  self.driver.find_element_by_xpath("//a[contains(text(), 'Shop')]").click()
