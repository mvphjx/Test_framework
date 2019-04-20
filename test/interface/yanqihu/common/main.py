from test.interface.yanqihu.common.get_team import GetTeam
from test.interface.yanqihu.common.get_team_data import GetTeamData
from utils.str.string_util import StringUtil
import logging

# 日志配置
logging.basicConfig(level=logging.INFO)


teams = GetTeam().getTeams()
logging.info("队伍总数：%d", len(teams))
test = []
test.append(teams[0])
teams = test
for team in teams:
    logging.info('开始获取队伍:%s', team['name'] + team['id'])
    PicList, VedioList = GetTeamData().getJson(team['id'])
    groupname = team['name'] + team['id']
    groupname = StringUtil().get_ch_en(groupname)
    logging.info('开始获取队伍图片,数量:%d', len(PicList))
    for pic in PicList:
        logging.info('正在获取图片：%s', pic['TaskName'] + pic['Path'])
        res = GetTeamData().getImg(pic['Path'])
        taskname = pic['TaskName']
        taskname = StringUtil().get_ch_en(taskname)
        if res.status_code == 200:
            GetTeamData().save_file(res, taskname + '.jpg', groupname)
        else:
            logging.warning('获取图片失败')
    logging.info('开始获取队伍视频,数量:%d', len(VedioList))
    for vedio in VedioList:
        logging.info('正在获取视频:%s' , vedio['TaskName']+vedio['Path'])
        res = GetTeamData().getVedio(vedio['Path'])
        if res.status_code == 200:
            GetTeamData().save_file(res, vedio['TaskName'] + ".mp4", groupname)
        else:
            logging.warning('获取视频失败')
