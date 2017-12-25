import time
import unittest

from selenium.webdriver.common.by import By

from test.ui.abisweb.case.login import Login
from test.ui.abisweb.case.lpcase import LpCase
from test.ui.abisweb.case.tpscan import TpScan
from utils.config import Config, DATA_PATH


class TestAbisMain(unittest.TestCase):
    URL = Config().get('URL')
    FILE_PATH = Config().get('TPIMG')
    excel = DATA_PATH + '/abis.xlsx'

    def sub_tearDown(self):
        self.page.quit()

    def query(self, cardNum):
        # 测试查询列表
        self.page.execute(' window.location="/abisweb/tp/list/"')
        time.sleep(3)
        self.page.find_element(*(By.ID, 'CARD_NUM')).send_keys(cardNum)
        self.page.find_element(*(By.ID, 'qryId_searchConId_txt')).click()
        time.sleep(3)
        #self.page.find_element(*(By.LINK_TEXT, cardNum)).click()

    def test_abis(self):
            with self.subTest(data="TpScan"):
                self.page = Login().run()
                time.sleep(3)
                self.tpcard_num = TpScan(self.page).run()
                time.sleep(2)
                self.sub_tearDown()
            with self.subTest(data="LpCase"):
                self.page = Login().run()
                time.sleep(3)
                self.lpcase_num = LpCase(self.page).run()
                time.sleep(2)
                self.sub_tearDown()

