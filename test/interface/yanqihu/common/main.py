from test.interface.yanqihu.common.get_team import GetTeam
from test.interface.yanqihu.common.get_team_data import GetTeamData
from utils.str.string_util import StringUtil

teams = GetTeam().getTeams()
print("队伍总数："+teams.__len__().__str__())
for team in teams:
    PicList, VedioList = GetTeamData().getJson(team['id'])
    groupname = team['name']+team['id']
    groupname = StringUtil().get_ch_en(groupname)
    for pic in PicList:
        res = GetTeamData().getImg(pic['Path'])
        taskname = pic['TaskName']
        taskname = StringUtil().get_ch_en(taskname)
        if res.status_code == 200:
            print(pic['TaskName'], pic['Path'])
            GetTeamData().save_file(res, taskname + '.jpg', groupname)
    # print(VedioList)
    # for vedio in VedioList:
    #     res = GetTeamData().getVedio(vedio['Path'])
    #     if res.status_code == 200:
    #         print(vedio['TaskName'], vedio['Path'])
    #         GetTeamData().save_file(res, vedio['TaskName'] + ".mp4", groupname)
