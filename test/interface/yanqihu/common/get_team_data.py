import os
import urllib

import re

from utils.client import HTTPClient
from utils.extractor import JMESPathExtractor
import json

'''
通过队伍id 队伍的图片视频信息
'''


class GetTeamData:
    def __init__(self):
        self.params = {'GameId': '', 'GTId': ''}
        self.base_url = 'http://server.goteaming.com.cn/'
        self.url = 'http://server.goteaming.com.cn/Player_Base/Game/GetTeamDataSource'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'}
        self.basepath = 'C:/test/'

    def getJson(self, GTId):
        self.params['GTId'] = GTId
        client = HTTPClient(url=self.url, method='POST', headers=self.headers)
        res = client.send(params=self.params)
        print(res.text)
        j = JMESPathExtractor()
        VedioList = j.extract(query='VedioList[]', body=res.text)
        PicList = j.extract(query='PicList[]', body=res.text)
        return PicList, VedioList

    def getImg(self, path):
        client = HTTPClient(url=self.base_url + path, method='Get')
        res = client.send(params=self.params)
        return res

    def getVedio(self, path):
        client = HTTPClient(url=self.base_url + path, method='Get', headers=self.headers)
        res = client.send(params=self.params)
        return res

    def saveVedio(self, path, name):
        self.mkdir(self.basepath + self.params['GTId'])
        urllib.request.urlretrieve(self.base_url + path, self.basepath + self.params['GTId'] + '%s.mp4' % (name))

    # 文件流,文件名-保存
    def save_file(self, res, fileName, groupname):
        self.mkdir(self.basepath + groupname)
        with open(self.basepath + groupname + '/' + fileName, "wb") as code:
            code.write(res.content)
        print(self.basepath + groupname + '/' + fileName)

    # 创建新目录
    def mkdir(self, path):
        path = path.strip()
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            return False


if __name__ == '__main__':
    PicList, VedioList = GetTeamData().getJson("631c027a-e792-4183-8b92-ae226c48ea83")
    PicList, VedioList = GetTeamData().getJson("2cba2415-0730-4c89-ba5d-83843502c90b")
    print(PicList)
    for pic in PicList:
        res = GetTeamData().getImg(pic['Path'])
        if res.status_code == 200:
            print(pic['TaskName'], pic['Path'])
            GetTeamData().save_file(res, pic['TaskName'] + '.jpg', '队名XXX')
    print(VedioList)
    for vedio in VedioList:
        res = GetTeamData().getVedio(vedio['Path'])
        if res.status_code == 200:
            print(vedio['TaskName'], vedio['Path'])
            GetTeamData().save_file(res, vedio['TaskName'] + ".mp4", '队名XXX')
