import time
import unittest

from selenium.webdriver.common.by import By

from test.ui.abisweb.case.login import Login
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
        return self.add()

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
        print(msg.text)
        return self.ABIS_CE_NUM

if __name__ == '__main__':
    URL = Config().get('URL')
    page = Login().run()
    LpCase(page).run()