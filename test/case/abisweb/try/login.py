import time

from selenium.webdriver.common.by import By

from test.page.abis_main_page import AbisMainPage
from utils.config import Config
from utils.log import logger

class Login:

    def __init__(self):
        URL = "http://www.baidu.com"
        self.page = AbisMainPage(browser_type='chrome').get(URL, maximize_window=True)


    def run(self):
        self.login()
        time.sleep(3)
        return  self.page
    def login(self):
        # 登录
        self.page.find_element(*(By.ID, 'kw')).send_keys("韩健祥")
        self.page.find_element(*(By.ID, 'su')).click()
if __name__ == '__main__':

    page=Login().run()
    print(page)
    page.quit()
    print(page)