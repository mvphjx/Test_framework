import re

import time


class StringUtil:
    # 获取中英文字符串
    def get_ch_en(self, string=""):
        if type(string) == str:
            try:
                res = re.findall(r'[\u4e00-\u9fa5a-zA-Z0-9]', string)
            except :
                print (string)
            result = ''
            for char in res:
                result = result + char
        else:
            result = time.time().__str__()
        return result
