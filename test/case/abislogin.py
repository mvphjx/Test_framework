import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://192.168.128.145:7950/abisweb"
base_path = os.path.dirname(os.path.abspath(__file__)) + '\..\..'
driver_path = os.path.abspath(base_path+'\drivers\IEDriverServer.exe')

locator_UserName = (By.ID, 'UserName')
locator_PassWord = (By.ID, 'PassWord')
locator_login = (By.ID, 'loginbutton')
driver = webdriver.Ie(executable_path=driver_path)
driver.get(URL)
driver.find_element(*locator_UserName).send_keys('han')
driver.find_element(*locator_PassWord).send_keys('4690255')
driver.find_element(*locator_login).click()
time.sleep(10)
driver.execute_script('alert(1)');
#driver.quit()
