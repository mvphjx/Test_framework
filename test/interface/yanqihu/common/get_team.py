from utils.client import HTTPClient
from bs4 import BeautifulSoup
'''
获取队伍id
'''

class GetTeam:
    def __init__(self):
        self.url = 'http://server.goteaming.com.cn/Player_Base/Game/ActivityFinish'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'}
        self.params = {'GameId': 'e6693b01-7b38-4413-a991-1d268190f190'}

    def getTeams(self):
        client = HTTPClient(url=self.url, method='GET')
        res = client.send(params=self.params)
        #print(res.text)
        soup = BeautifulSoup(res.text,"html.parser")
        team_divs = soup.select(".Team")
        # <div class="Team active" gtid="a614ae1c-597a-431d-8134-de681cdabca3">队伍3</div>
        teams = []
        for  team_div in team_divs:
            #print(team_div.get_text(),team_div.get('gtid'))
            teams.append({'name':team_div.get_text(),'id':team_div.get('gtid')})
        return    teams;





if __name__ == '__main__':
    teams =GetTeam().getTeams()
    print(teams[1])
