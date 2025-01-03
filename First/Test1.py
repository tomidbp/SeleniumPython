from selenium import webdriver

#PATH = "D:\Code\chromedriver.exe"
#driver = webdriver.Chrome(PATH) --- webdriver was installed in python scripts folder, and it does not requires path specification anymore!
driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element_by_name("username").send_keys("Admin")
driver.find_element_by_name("password").send_keys("admin123")
driver.find_element_by_class_name("oxd-button").click()

act_title = driver.title
exp_title="OrangeHRM"

if act_title == exp_title:
  print("Login Test Passed")
else:
  print("Login Test Failed")

driver.close()
