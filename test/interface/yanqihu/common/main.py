from test.interface.yanqihu.common.get_team import GetTeam
from test.interface.yanqihu.common.get_team_data import GetTeamData

teams =GetTeam().getTeams()
for team in teams :
    PicList, VedioList = GetTeamData().getJson(team['id'])
    groupname = team['name']
    for pic in PicList:
        print(pic['TaskName'],pic['Path'])
        file_data=GetTeamData().getImg(pic['Path'])
        GetTeamData().save_file(file_data,pic['TaskName']+'.jpg',groupname)
    for vedio in VedioList:
        print(vedio['TaskName'],vedio['Path'])
        res = GetTeamData().getVedio(vedio['Path'])
        GetTeamData().save_file(res,vedio['TaskName']+".mp4",groupname)
