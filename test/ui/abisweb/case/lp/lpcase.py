import time
import unittest

from selenium.webdriver.common.by import By

from test.ui.abisweb.case.login import Login
from utils.assertion import assertWebDialogMsg, assertWebTableSearchOne
from utils.config import Config


class LpCase:

    def __init__(self, page):
        """
        :param page: test.common.page
        """
        self.page = page
        self.CE_NUM = Config().get('CE_NUM')
        self.ABIS_CE_NUM = Config().get('ABIS_CE_NUM')

    def run(self):
        self.add()
        self.query()
        return self.ABIS_CE_NUM

    def add(self):
        # 案件录入
        self.page.execute(' window.location="/abisweb/lp/lpinputedit/"')
        time.sleep(3)
        self.page.find_element(*(By.ID, 'CE_NUM')).send_keys(self.CE_NUM)
        self.page.find_element(*(By.ID, 'ABIS_CE_NUM')).send_keys(self.ABIS_CE_NUM)
        self.page.find_element(*(By.ID, 'CE_NAME')).send_keys("seleniumCaseTest")
        self.page.find_element(*(By.ID, 'submit1')).click()
        time.sleep(1)
        msg = self.page.find_element(*(By.CLASS_NAME, 'dialogtext'))
        assertWebDialogMsg(msg.text)

    def query(self):
        # 测试查询列表
        self.page.execute(' window.location="/abisweb/lp/caselist/"')
        time.sleep(3)
        self.page.find_element(*(By.ID, 'ABIS_CE_NUM')).send_keys(self.ABIS_CE_NUM)
        self.page.find_element(*(By.ID, 'qryId_searchConId_txt')).click()
        time.sleep(3)
        assertWebTableSearchOne(self.page)


if __name__ == '__main__':
    page = Login().run()
    LpCase(page).run()
