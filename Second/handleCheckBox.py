from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.find_element(By.ID, "cookieChoiceDismiss").click()

# 1 select specific checkbox
#driver.find_element(By.XPATH, "//input[@id='monday']").click()

#2) select all checkboxes

checkboxes=driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")

print(len(checkboxes)) 

#Approach1

#for i in range(len(checkboxes)):
#  checkboxes[i].click()
  
#Approach2

#for checkbox in checkboxes:
#  checkbox.click()
  
#3) Select multiple checkboxes by choice

#for checkbox in checkboxes:
#  weekname=checkbox.get_attribute('id')
#  if weekname=='monday' or weekname=='sunday':
#      checkbox.click()

#4) Select last 2 checkboxes
#range(5,7) --> 6,7
# totalnumbersofelements-2= starting index (7(total number) - 2(the last two checkboxes)) = 6,7 (counting always starts from 0, so +1 to the total number) 

#for i in range(len(checkboxes)-2,len(checkboxes)): 
#  checkboxes[i].click()
  
#5) select first 2  
#for i in range(len(checkboxes)): 
#  if i<2:
#    checkboxes[i].click()

#6) clearing all the checkboxes
#for checkbox in checkboxes:
#  if checkbox.is_selected():
#    checkbox.click()