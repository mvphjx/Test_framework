from utils.client import HTTPClient
from utils.extractor import JMESPathExtractor

url  = 'http://server.goteaming.com.cn/Player_Base/Game/GetTeamDataSource'
headers={'User-Agent':'Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'}
client = HTTPClient(url=url, method='POST',headers=headers)
params = {'GameId':'e6693b01-7b38-4413-a991-1d268190f190','GTId':'a840bc77-07b8-4d49-9047-22176dda6986'}
res = client.send(params=params)
print(res.text)
j = JMESPathExtractor()
VedioList = j.extract(query='VedioList[]', body=res.text)
PicList = j.extract(query='PicList[]', body=res.text)
