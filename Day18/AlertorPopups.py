import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\nbiswal\\Desktop\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# Open url
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(4)

alertwindow = driver.switch_to.alert
print(alertwindow.text)
alertwindow.send_keys("welcome")
alertwindow.dismiss()
time.sleep(2)
#driver.close()




