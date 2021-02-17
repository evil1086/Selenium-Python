import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(r"C:\Users\vin\PycharmProjects\seleniumTest01\Browsers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

"""
Implicitly wait Demo
driver.implicitly_wait(5)
driver.find_element_by_css_selector("input.search-keyword").send_keys("cu")
time.sleep(4)

count = len(driver.find_elements_by_xpath("//div[@class = 'products']/div"))

assert count == 2
buttons = driver.find_elements_by_xpath("//div[@class = 'product-action']/button")

for button in buttons:
    button.click()

driver.find_element_by_css_selector("img[alt = 'Cart']").click()
driver.find_element_by_css_selector("div[class = 'action-block'] button").click()

driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button.promoBtn").click()
print(driver.find_element_by_css_selector("span.promoInfo").text)
"""
# Explicitly wait Demo
driver.implicitly_wait(7)

list1 = []
list2 = []
list3 = []
list4 = []
total = 0
driver.find_element_by_css_selector("input.search-keyword").send_keys("cu")
time.sleep(4)

count = len(driver.find_elements_by_xpath("//div[@class = 'products']/div"))

assert count == 2
print('Product count verified')
buttons = driver.find_elements_by_xpath("//div[@class = 'product-action']/button")
# traversing from child to parent ----> //div[@class = 'product-action']/button/parent::div/parent::div/h4

veggi_name = driver.find_elements_by_xpath("//h4[@class = 'product-name']")
for veggi in veggi_name:
    list1.append(veggi.text)

print(list1)

for button in buttons:
    # print(button.find_elements_by_xpath("parent::div/parent::div/h4").text)
    button.click()

driver.find_element_by_css_selector("img[alt = 'Cart']").click()
cart_veggi_list  = driver.find_elements_by_css_selector("p.product-name")

for cart_veggi in cart_veggi_list:
    if cart_veggi != '':
        list3.append(cart_veggi.text)

print(list3)
driver.find_element_by_css_selector("div[class = 'action-block'] button").click()

veggi_summary = driver.find_elements_by_css_selector("p.product-name")

for vegg in veggi_summary:
    if vegg.text != '':
        list2.append(vegg.text)

print(list2)

assert list1 == list2
print("Marketplace and summary page having the same list of veggies")
#wait = WebDriverWait(driver, 5)
#wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input.promoCode")))
original_amount = float(driver.find_element_by_css_selector("span.discountAmt").text)
driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button.promoBtn").click()

#wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
print(driver.find_element_by_css_selector("span.promoInfo").text)

discounted_price = float(driver.find_element_by_css_selector("span.discountAmt").text)

sums = driver.find_elements_by_xpath("//tr/td[5]/p")

summary_veggi_list = driver.find_elements_by_xpath("//tr/td[2]/p")

for summary_veggi in summary_veggi_list:
    if summary_veggi != '':
        list4.append(summary_veggi.text)
print(list4)

assert list3 == list3
print("Cart and summary page content are the same ")

for sum in sums:
    total += int(sum.text)

print(total)
assert total == original_amount

assert discounted_price < original_amount
driver.close()
