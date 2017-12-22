import time
import unittest

import win32con
import win32gui
from selenium.webdriver.common.by import By

from test.page.abis_main_page import AbisMainPage


class TestTpScan(unittest.TestCase):
    # URL = Config().get('URL')
    URL = "http://192.168.129.107:7950/abisweb"
    FILE_PATH = 'C:\\test\\1.bmp'
    def login(self):
        # 登录
        print(self.URL)
        self.page = AbisMainPage(browser_type='ie').get(self.URL, maximize_window=False)
        locator_UserName = (By.ID, 'UserName')
        locator_PassWord = (By.ID, 'PassWord')
        locator_login = (By.ID, 'loginbutton')
        self.page.find_element(*locator_UserName).send_keys('han')
        self.page.find_element(*locator_PassWord).send_keys('4690255')
        self.page.find_element(*locator_login).click()

    def sub_tearDown(self):
        self.page.quit()

    @AbisMainPage.async
    def operation_dialog(self):
        #操作系统文件上传
        time.sleep(2)
        # win32gui
        dialog = win32gui.FindWindow('#32770', '打开')  # 对话框
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, self.FILE_PATH)  # 往输入框输入绝对地址
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button


    def scan(self):
        #捺印录入
        self.page.execute(' window.location="/abisweb/tp/scan/"')
        time.sleep(3)
        self.operation_dialog()
        self.page.execute(' $(".ImportImg").click()')
        time.sleep(2)
        self.page.execute(' $("#ScanObjectTree_1_span").dblclick()')
        self.page.find_element(*(By.ID, 'AutoSplit')).click()
        self.page.find_element(*(By.ID, 'ShowTxt')).click()
        self.page.find_element(*(By.ID, 'NAME')).send_keys('seleniumTest')
        time.sleep(1)
        personNum = self.page.find_element(*(By.ID, 'PERSON_NUM')).get_attribute("value")
        cardNum = self.page.find_element(*(By.ID, 'CARD_NUM')).get_attribute("value")
        print("personNum:" + personNum)
        print("cardNum:" + cardNum)
        self.page.find_element(*(By.ID, 'Save')).click()
        return cardNum

    def query(self, cardNum):
        # 测试查询列表
        self.page.execute(' window.location="/abisweb/tp/list/"')
        time.sleep(3)
        self.page.find_element(*(By.ID, 'CARD_NUM')).send_keys(cardNum)
        self.page.find_element(*(By.ID, 'qryId_searchConId_txt')).click()
        time.sleep(3)
        #self.page.find_element(*(By.LINK_TEXT, cardNum)).click()

    def test_tp(self):

        self.login()
        time.sleep(3)
        cardNum = self.scan()
        self.sub_tearDown()

        self.login()
        time.sleep(3)
        self.query(cardNum)
        self.sub_tearDown()
