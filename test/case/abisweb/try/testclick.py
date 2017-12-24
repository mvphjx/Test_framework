import unittest

import time
from selenium.webdriver.common.by import By

from test.page.abis_main_page import AbisMainPage


class TestGitHub():
    URL = "https://mvphjx.github.io/starDemo/LearnAndTest/a.html"
    #<div class="_box"><a href="#" onclick="window.open('upload.html')">选择图片</a></div>
    locator_result = (By.XPATH, '//div[contains(@class, "_box")]/a')

    def __init__(self,type):
        self.page = AbisMainPage(browser_type=type).get(self.URL, maximize_window=True)


    def run(self):
        link = self.page.find_element(*self.locator_result)
        link.click()
        time.sleep(3)
        print("after click:"+self.page.current_url)
        self.page.switch_to_window()
        print("after switch_to_window1:"+self.page.current_url)
        self.page.switch_to_window()
        print("after switch_to_window2:"+self.page.current_url)



if __name__ == '__main__':
    #TestGitHub("ie").run()
    TestGitHub("chrome").run()