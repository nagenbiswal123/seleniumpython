import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\nbiswal\\Desktop\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# Open url
driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH, "//input[@value='Login']").click() # LOGIN BUTTON
myalert = driver.switch_to.alert
print(myalert .text)
myalert.dismiss()

time.sleep(2)

driver.quit()