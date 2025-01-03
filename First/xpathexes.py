from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("D:\\Code\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

#Self

#text_msg=driver.find_element(By.XPATH, "//a[contains(text(),'Delta Corp Ltd.')]/self::a").text
#print(text_msg) #Delta Corp Ltd.

#Parent

#text_msg=driver.find_element(By.XPATH, "//a[contains(text(),'Delta Corp Ltd.')]/parent::td").text
#print(text_msg) #Delta Corp Ltd.

#Child

#child=driver.find_elements(By.XPATH, "//a[contains(text(),'Delta Corp Ltd.')]/ancestor::tr/child::td")
#print(len(child)) #6

#Ancestor

#text_msg=driver.find_element(By.XPATH, "//a[contains(text(),'Delta Corp Ltd.')]/ancestor::tr").text
#print(text_msg) #Delta Corp Ltd. A 121.45 134.95 + 11.12 Buy  |  Sell

#Descendant

#descendant=driver.find_elements(By.XPATH, "//a[contains(text(),'Delta Corp Ltd.')]/ancestor::tr/descendant::*")
#print(len(descendant)) #10

#Following

#following=driver.find_elements(By.XPATH, "//a[contains(text(),'Delta Corp Ltd.')]/ancestor::tr/following::*")
#print("Number of descendant nodes:",len(following)) #4782

#Following-siblings

#followingsibling=driver.find_elements(By.XPATH, "//a[contains(text(),'Delta Corp Ltd.')]/ancestor::tr/following-sibling::*")
#print("Number of descendant nodes:",len(followingsibling)) #421

#Preceding

#preceding=driver.find_elements(By.XPATH, "//a[contains(text(),'Delta Corp Ltd.')]/ancestor::tr/preceding::*")
#print(len(preceding)) #212

#Preceding-Sibling

#precedingsibling=driver.find_elements(By.XPATH, "//a[contains(text(),'Delta Corp Ltd.')]/ancestor::tr/preceding-sibling::tr")
#print(len(precedingsibling)) #4