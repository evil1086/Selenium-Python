from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\vin\PycharmProjects\seleniumTest01\Browsers\chromedriver.exe")


driver.get("http://demo.guru99.com/test/radio.html")
checkboxes = driver.find_elements_by_xpath("//input[@type = 'checkbox']")
print('lengths of list is = ', len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute('value') == 'checkbox2':
        checkbox.click()
        assert checkbox.is_selected()

radiobuttons = driver.find_elements_by_css_selector("input[type = 'radio']")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()


driver.get("http://demo.guru99.com/test/delete_customer.php")

test_text = 'Customer'
driver.find_element_by_css_selector("input[name='cusid']").send_keys("vinod")
driver.find_element_by_css_selector("input[name='submit']").click()
alert = driver.switch_to.alert
alert_text = alert.text
assert test_text in alert_text
print('assertion is working as expected')
alert.accept()
driver.close()
