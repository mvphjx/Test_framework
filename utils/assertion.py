"""
在这里添加各种自定义的断言，断言失败抛出AssertionError就OK。
"""


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
