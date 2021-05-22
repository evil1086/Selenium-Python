from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\vin\PycharmProjects\seleniumTest01\Browsers\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("body[id= 'tinymce']").clear()
driver.find_element_by_css_selector("body[id= 'tinymce']").send_keys("This is test example")
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)

driver.close()
