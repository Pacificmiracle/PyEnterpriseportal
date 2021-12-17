import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://ep.customer.server247.info/login")
wait = WebDriverWait(driver, 10)
driver.find_element_by_id("email").click()
driver.find_element_by_id("email").send_keys("prashant.basnet@yopmail.com")
driver.find_element_by_id("password").click()
driver.find_element_by_id("password").send_keys("Amnil@123")
driver.find_element_by_id("acceptTerms").click()
driver.find_element_by_xpath("/html/body/app-root/abp-dynamic-layout/abp-layout-application/div/app-login/div/div/div[1]/div/div[1]/form/button").click()
driver.find_element_by_id("optCode").click()
driver.find_element_by_id("optCode").send_keys("8")
wait = WebDriverWait(driver, 10)
driver.find_element_by_css_selector(".btn").click()
print(driver.current_url)
print(driver.title)
print(driver.page_source)
time.sleep(15)
driver.quit()
