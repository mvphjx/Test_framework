import time
import unittest

from selenium.webdriver.common.by import By

from test.case.abisweb.tpimg_upload import tpimgUload
from utils.config import Config


class LpCase:

    def __init__(self, page):
        """
        :param page: test.common.page
        """
        self.page = page

    def run(self):
        self.add()

    def add(self):
        # 案件录入
        self.page.execute(' window.location="/abisweb/tp/scan/"')
        time.sleep(3)
        case_num = "A1234354555"
        return case_num
