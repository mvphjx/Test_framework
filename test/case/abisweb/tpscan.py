import time
import unittest
from utils.log import logger
from selenium.webdriver.common.by import By

from test.case.abisweb.login import Login
from test.case.abisweb.tpimg_upload import tpimgUload
from test.page.abis_main_page import AbisMainPage
from utils.config import Config


class TpScan:

    def __init__(self, page):
        """

        :param page: test.common.page
        """
        self.image = Config().get('TPIMAGE')
        self.page = page

    def run(self):
        self.scan()

    def scan(self):
        # 捺印录入
        self.page.execute(' window.location="/abisweb/tp/scan/"')
        time.sleep(3)
        tpimgUload.operation_dialog()
        self.page.execute(' $(".ImportImg").click()')
        time.sleep(2)
        self.page.execute(' $("#ScanObjectTree_1_span").dblclick()')
        self.page.find_element(*(By.ID, 'AutoSplit')).click()
        self.page.find_element(*(By.ID, 'ShowTxt')).click()
        self.page.find_element(*(By.ID, 'NAME')).send_keys('seleniumTest')
        time.sleep(1)
        personNum = self.page.find_element(*(By.ID, 'PERSON_NUM')).get_attribute("value")
        cardNum = self.page.find_element(*(By.ID, 'CARD_NUM')).get_attribute("value")
        logger.info("personNum:" + personNum)
        logger.info("cardNum:" + cardNum)
        self.page.find_element(*(By.ID, 'Save')).click()
        return cardNum

if __name__ == '__main__':
    URL = Config().get('URL')
    page = AbisMainPage(browser_type='ie').get(URL, maximize_window=False)
    Login(page).run()
    TpScan(page).run()
    #page.quit();