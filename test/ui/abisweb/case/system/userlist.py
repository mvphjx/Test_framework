import time
import unittest

from selenium.webdriver.common.by import By

from test.ui.abisweb.case.login import Login
from test.ui.abisweb.case.lpcase import LpCase
from test.ui.abisweb.case.tpscan import TpScan
from utils.assertion import assertWebTableSearch
from utils.config import Config, DATA_PATH
'''
用户列表查询测试
'''

class UserList:
    def __init__(self, page):
        """
        :param page: test.common.page
        """
        self.page = page
        self.USER_ID = Config().get('USER_ID')

    def run(self):
        self.query()

    def query(self):
        # 测试查询列表
        self.page.execute(' window.location="/abisweb/user/list/"')
        time.sleep(3)
        self.page.find_element(*(By.ID, 'USER_ID')).send_keys(self.USER_ID)
        self.page.find_element(*(By.ID, 'qryId_searchConId_txt')).click()
        time.sleep(3)
        assertWebTableSearch(self.page)


if __name__ == '__main__':
    page = Login().run()
    UserList(page).run()
