from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("D:\\Code\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://demo.nopcommerce.com/")


#Absolute Xpath

#driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[2]/div[2]/form/input").send_keys("Books")
#driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[2]/div[2]/form/button").click()

#Relative Xpath

driver.find_element(By.XPATH, "//*[@id='small-searchterms']").send_keys("Books")
driver.find_element(By.XPATH, "//*[@id='small-search-box-form']/button").click()