import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

allLinks=driver.find_elements(By.TAG_NAME,'a')
count=0

for link in allLinks:
  url=link.get_attribute('href')
  
  try:
    res=requests.head(url)
  
  except:
    None
    
  if res.status_code>=400:
    print(url," Is broken link")
    count+=1
  else:
    print(url," is valid links")

print("Toatal number of broken links:", count)
