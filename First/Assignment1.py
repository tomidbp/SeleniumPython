from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://admin-demo.nopcommerce.com")

driver.find_element_by_name("Email").clear()
driver.find_element_by_name("Email").send_keys("admin@yourstore.com")

driver.find_element_by_name("Password").clear()
driver.find_element_by_name("Password").send_keys("admin")
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()

act_title = driver.title
exp_title = "Dashboard / nopCommerce administration"

if act_title == exp_title:
  print("Login Test Passed")
else:
  print("Login Test Failed")

driver.close()