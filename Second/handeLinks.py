from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.find_element(By.ID, "cookieChoiceDismiss").click() 

#click on the link
# driver.find_element(By.LINK_TEXT,"open cart").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"open").click()

#Find number of links in a page
# links=driver.find_elements(By.TAG_NAME,'a')
links=driver.find_elements(By.XPATH,'//a')
print("total number of links:", len(links))

#Print all the link names

for link in links:
  print(link.text)