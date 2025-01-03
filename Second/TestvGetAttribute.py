from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=options)
serv_obj=Service("D:\\Code\\chromedriver.exe")
driver=webdriver.Chrome(options=options)

driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://admin-demo.nopcommerce.com/login")

emailbox=driver.find_element(By.XPATH, "//input[@id='Email']")

emailbox.clear()
emailbox.send_keys(abc@gmail.com)

print("result of text:", emailbox.text)
print("result of get_attribute():", emailbox.get_attribute('value'))
