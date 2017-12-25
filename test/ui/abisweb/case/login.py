import time

from selenium.webdriver.common.by import By

from test.page.abis_main_page import AbisMainPage
from utils.config import Config
from utils.log import logger

class Login:

    def __init__(self):
        URL = Config().get('URL')
        self.page = AbisMainPage(browser_type='ie').get(URL, maximize_window=True)


    def run(self):
        self.login()
        time.sleep(3)
        return  self.page
    def login(self):
        # 登录
        locator_UserName = (By.ID, 'UserName')
        locator_PassWord = (By.ID, 'PassWord')
        locator_login = (By.ID, 'loginbutton')
        self.page.find_element(*locator_UserName).send_keys('han')
        self.page.find_element(*locator_PassWord).send_keys('4690255')
        self.page.find_element(*locator_login).click()
if __name__ == '__main__':

    page=Login().run()
    logger.info(page)
    #page.quit();