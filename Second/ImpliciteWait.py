from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=options)
driver.get("https://www.google.com/")
driver.maximize_window()


driver.find_element(By.CLASS_NAME, "QS5gu-sy4vM").click()


searchbox=driver.find_element(By.NAME, 'q')


searchbox.send_keys("Selenium")
searchbox.submit()


time.sleep(5)
driver.find_element(By.XPATH, "(//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Selenium'])[1]").click()



