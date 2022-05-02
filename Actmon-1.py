from selenium import webdriver
from selenium.webdriver.common.by import By

# path of the chrome driver
driver = webdriver.Chrome(executable_path="C:\\Users\\nbiswal\\Desktop\\chromedriver_win32\\chromedriver.exe")

#open url
driver.get("http://webapps.tekstac.com/InvoiceUpdates/")

#locate user
driver.find_element(by=By.NAME,value="Customer Name*").send_keys('Rakesh')


driver.find_element(by=By.XPATH,value="//input[@id='name']").send_keys("Rakesh")
driver.find_element(by=By.XPATH,value="//input[@id='number']").send_keys("123")
driver.find_element(by=By.XPATH,value="//input[@id='newUser']").click()
driver.find_element(by=By.XPATH,value="//tbody//tr//td//select").click()

driver.find_element(by=By.XPATH,value="//tbody/tr[6]/td[2]/input[1]").send_keys("1000")
driver.find_element(by=By.XPATH,value="//tbody/tr[7]/td[2]/input[1]").send_keys(9876543210)
driver.find_element(by=By.XPATH,value="//tbody/tr[8]/td[2]/textarea[1]").send_keys("New User Invoice'")
driver.find_element(by=By.XPATH,value="//input[@id='submit']").click()

print(driver.find_element(by=By.XPATH,value="//div[@id=" "]))