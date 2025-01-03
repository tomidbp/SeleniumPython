from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj=Service("D:\\Code\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

print(driver.title) #OrangeHRM
print(driver.current_url) #https://opensource-demo.orangehrmlive.com/
print(driver.page_source)

driver.quit()