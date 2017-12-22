import os
import time
import win32gui
import win32con
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://192.168.129.107:7950/abisweb"
base_path = os.path.dirname(os.path.abspath(__file__)) + '\..\..'
driver_path = os.path.abspath(base_path + '\drivers\IEDriverServer.exe')

locator_UserName = (By.ID, 'UserName')
locator_PassWord = (By.ID, 'PassWord')
locator_login = (By.ID, 'loginbutton')
driver = webdriver.Ie(executable_path=driver_path)
driver.get(URL)
driver.find_element(*locator_UserName).send_keys('han')
driver.find_element(*locator_PassWord).send_keys('4690255')
driver.find_element(*locator_login).click()
time.sleep(3)
driver.execute_script('window.location="/abisweb/import/fpt/"')
time.sleep(3)
print("to open")
driver.execute_script('$("#file_upload").click()')
time.sleep(3)
print("opening")
# win32gui
dialog = win32gui.FindWindow('#32770', '打开')  # 对话框
ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit1', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
button = win32gui.FindWindowEx(dialog, 0, 'Button1', None)  # 确定按钮Button
win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'D:\test\1.bmp')  # 往输入框输入绝对地址
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
# driver.quit()
