from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element(By.ID, "cookieChoiceDismiss").click()

drpCountry_element=driver.find_element(By.XPATH, "//select[@id='country']")

drpCountry=Select(drpCountry_element) # -> always write Select with capital S
# !!!drpCountry=select(driver.find_element(By.XPATH, "//select[@id='country']")) -> this can be used instead of the one above if you do not want to name the function!

#Select option from the dropdown
# drpCountry.select_by_visible_text("Germany")
# drpCountry.select_by_value("germany")
# drpCountry.select_by_index(3) #index

#capture all options and print them

allOptions=drpCountry.options
print("total number of options:",len(allOptions))

# for opt in allOptions:
#   print(opt.text)
  
  #select option from dropdown without using built-in method
# for opt in allOptions:
#   if opt.text=="Japan":
#     opt.click()
#     break


# driver.find_elements(By.XPATH, '//*[@id="country"]/option')
# print(len(allOptions)) -> in case "select is not available in the element"