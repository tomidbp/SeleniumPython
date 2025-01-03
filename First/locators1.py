from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\\Code\\chromedriver.exe")
driver = webdriver.Chrome(service = serv_obj)

driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://demo.nopcommerce.com/")

#id & name locators 
#driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
#driver.find_element(By.NAME, "q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

#Linktext & partial Linktext
#driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()
driver.find_element(By.LINK_TEXT, "Register").click()

#driver.close() #closes only one browser at the time
#driver.quit() #closes all browsers