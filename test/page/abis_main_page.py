from selenium.webdriver.common.by import By
from test.common.page import Page
from threading import Thread

class AbisMainPage(Page):
    loc_search_input = (By.ID, 'kw')
    loc_search_button = (By.ID, 'su')

    def search(self, kw):
        """搜索功能"""
        self.find_element(*self.loc_search_input).send_keys(kw)
        self.find_element(*self.loc_search_button).click()
