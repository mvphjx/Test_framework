"""
在这里添加各种自定义的断言，断言失败抛出AssertionError就OK。
"""
from selenium.webdriver.common.by import By


def assertHTTPCode(response, code_list=None):
    res_code = response.status_code
    if not code_list:
        code_list = [200]
    if res_code not in code_list:
        raise AssertionError('响应code不在列表中！')  # 抛出AssertionError，unittest会自动判别为用例Failure，不是Error


def assertWebDialogMsg(msg):
    errorWords = ["已经存在","已存在", "失败", "错误"]
    for keyWord in errorWords:
        if keyWord in msg:
            raise AssertionError('返回错误信息：' + msg)

'''
表格查询测试 判断是否检索成功
'''
def assertWebTableSearch(page):
    #总数
    count = page.find_element(*(By.CSS_SELECTOR, '.RecordCnt'))
    if count.text!= '总数:1':
        raise AssertionError('列表查询数据总数为' + count.text)
    elements = page.find_elements(*(By.CSS_SELECTOR, '.cell_min_w'))
    result = '查询结果：'
    for element in elements:
        result=result+element.text+" "
    print(result)
