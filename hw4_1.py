from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com")
search = driver.find_element_by_name("q")
search.send_keys("selenium install ubuntu python", Keys.RETURN)
result = driver.find_element_by_partial_link_text("pypi.org")
result.click()
second_result = driver.find_element_by_name("q")
second_result.send_keys("selenium library", Keys.RETURN)
second_result = driver.find_elements_by_class_name("package-snippet")
second_result.click()
driver.close()