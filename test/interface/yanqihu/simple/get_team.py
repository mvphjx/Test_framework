from utils.client import HTTPClient

url  = 'http://server.goteaming.com.cn/Player_Base/Game/ActivityFinish'
client = HTTPClient(url=url, method='GET')
headers={'User-Agent':'Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'}
params = {'GameId':'e6693b01-7b38-4413-a991-1d268190f190'}
res = client.send(params=params)
print(res.text)