import time

from pykeyboard import PyKeyboard
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from test.page.abis_main_page import AbisMainPage
from utils.log import logger


class Read:

    def __init__(self):
        URL = "https://weread.qq.com/"
        # URL = "https://keyboard.51240.com"
        # chrome firefox ie
        self.page = AbisMainPage(browser_type='firefox').get(URL, maximize_window=True)
        self.keyAction = ActionChains(self.page.driver)
        self.k = PyKeyboard()
        self.count=0
        self.preTitle=''
        self.thisTitle='0'
        self.sameCount = 0
    def run(self):
        time.sleep(10)
        while (self.next()):
            self.save()
        time.sleep(10)
        return  self.page
    def save(self):
        # 保存网页
        title = (By.CLASS_NAME, 'readerTopBar_title_chapter')
        try:
            titleEle = self.page.find_element(*title)
        except Exception as e:
            titleEle = None
        if not titleEle:
            return 0
        text=titleEle.text
        self.preTitle = self.thisTitle
        self.thisTitle = text
        if self.preTitle==self.thisTitle:
            return 0
        self.count = self.count+1
        # self.keyAction.key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
        # logger.info("key_down ctrl+s")
        # self.keyAction.key_down(Keys.CONTROL).key_down('s').key_up(Keys.CONTROL).key_up('s').perform()
        self.k.press_keys([self.k.control_l_key, 's'])
        time.sleep(1)
        for i in range(9):
            time.sleep(0.1)
            self.k.press_key(self.k.left_key)
        countStr = str(self.count)
        for everyChar in countStr:
            time.sleep(0.1)
            self.k.press_key(everyChar)
        time.sleep(0.1)
        self.k.press_key(self.k.enter_key)
        time.sleep(2)
        logger.info("下载...."+text+"-"+str(self.count))
        self.k.press_key(self.k.right_key)
        time.sleep(3)
    def next(self):
        if self.preTitle=='':
            logger.info("等待开始下载....")
            time.sleep(3)
            return True
        if self.preTitle==self.thisTitle:
            logger.info("下载完成....")
            return False
        logger.info("继续下载....")
        return True

    def quit(self):
        self.page.driver.quit()
if __name__ == '__main__':
    page=Read().run()