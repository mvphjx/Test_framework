import time
import unittest

import win32gui

import win32con
from selenium.webdriver.common.by import By

from test.page.abis_main_page import AbisMainPage
from utils.HTMLTestRunner import HTMLTestRunner
from utils.config import DATA_PATH, REPORT_PATH


class TestTpScan(unittest.TestCase):
    #URL = Config().get('URL')
    URL = "http://192.168.129.107:7950/abisweb"
    excel = DATA_PATH + '/baidu.xlsx'

    def sub_setUp(self):
        # 初始页面是main page，传入浏览器类型打开浏览器
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

    def test_scan(self):
        self.sub_setUp()
        time.sleep(3)
        self.page.execute(' window.location="/abisweb/tp/scan/"')
        time.sleep(3)
        print("to open")
        self.page.execute_async(' $(".ImportImg").click()')
        #self.page.find_element((By.ID, 'ScanOcx')).sendKeys('D:\test\1.bmp')

        time.sleep(3)
        print("opening")
        # win32gui
        # dialog = win32gui.FindWindow('#32770', '打开')  # 对话框
        # ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        # ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        # Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit1', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        # button = win32gui.FindWindowEx(dialog, 0, 'Button1', None)  # 确定按钮Button
        # win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'D:\test\1.bmp')  # 往输入框输入绝对地址
        # win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button






if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架 灰蓝', description='修改html报告')
        runner.run(TestTpScan('test_scan'))
    # e = Email(title='百度搜素测试报告',
    #           message='这是今天的测试报告，请查收！',
    #           receiver='396214358@qq.com',
    #           server='...',
    #           sender='...',
    #           password='...',
    #           path=report
    #           )
    # e.send()
