import re

from test.interface.yanqihu.common.get_team import GetTeam
from test.interface.yanqihu.common.get_team_data import GetTeamData
from utils.str.string_util import StringUtil

teams = GetTeam().getTeams()
print("队伍总数：" + teams.__len__().__str__())
for team in teams:
    PicList, VedioList = GetTeamData().getJson(team['id'])
    groupname = team['name']+team['id']
    groupname = StringUtil().get_ch_en(groupname)
    for pic in PicList:
        taskname = pic['TaskName']
        taskname = StringUtil().get_ch_en(taskname)
        GetTeamData().mkdir("c:/test2/" + taskname)
