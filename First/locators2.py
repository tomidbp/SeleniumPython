from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\\Code\\chromedriver.exe")
driver = webdriver.Chrome(service = serv_obj)

driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.facebook.com")

#Tag and Id combinations
#driver.find_element(By.CSS_SELECTOR, "input#email").send.keys("abc")
#driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc")

# tag and class 
#driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abc@gmail.com")
#driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("abc@gmail.com")

#Tag and attribute combination - tag is optional
#driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_email]").send_keys("abc@gmail.com")
#driver.find_element(By.CSS_SELECTOR, "[data-testid=royal_email]").send_keys("abc@gmail.com")

#tag , class and attribute
driver.find_element(By.CSS_SELECTOR, " input.inputtext[data-testid=royal_pass]").send_keys("xyz")