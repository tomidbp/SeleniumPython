from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj=Service("D:\\Code\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/register")