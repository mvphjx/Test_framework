from utils.database.util.oracle import OracleConnection

connection = OracleConnection().connection

sql_hit = "SELECT * FROM HIT_STAT_LTL_HIT_INFO WHERE BATCH_NUM = 'zhejiang830LT'  ";
sql_task = "SELECT * FROM QRY_TASK WHERE to_char(SUBMIT_TIME) IN ('26-12月-17', '25-12月-17') AND SUBMIT_USER IN ('fuzhanbao', 'zhenguojing')";
sql_cand = "SELECT  LOC_CARD_NUM AS LOC_CARD_NUM,FGP,QRY_ID FROM QRY_CAND";

'''
1 遍历比对任务
2 遍历比对任务之下的候选卡
3 与比中数据  进行匹配
4 过滤重复的比对任务
'''
tasks = connection.cursor()  # 创建 比对任务cursor
tasks.execute(sql_task)
count = 0
result = [];
result_first_src_card_nums = []
for task_values in tasks:
    find = False  # 是否找到匹配的 比中关系
    first_src_card_num = task_values[35]
    sql_cand_new = sql_cand + " where QRY_ID =" + str(task_values[0])
    cands = connection.cursor()  # 创建 候选卡cursor
    cands.execute(sql_cand_new)
    for cand_values in cands:
        loc_card_num = cand_values[0]
        cand_fgp = cand_values[1]
        qry_id = cand_values[2]
        hits = connection.cursor()  # 创建 比中数据cursor
        hits.execute(sql_hit)
        for hit_values in hits:
            # 获取比中关系中可用的数据
            person_num = hit_values[0]
            if hit_values[5] == None:
                tp_card_num = hit_values[0].replace("R", "");
            else:
                tp_card_num = hit_values[5]
            ce_num = hit_values[7]
            if hit_values[10] == None:
                lp_card_num = hit_values[7] + str(hit_values[8])
            else:
                lp_card_num = hit_values[10]
            bty = hit_values[12]
            fgp = hit_values[13]
            qry_type = hit_values[16]
            batch_num = hit_values[18]
            # print("tp_card_num:" + tp_card_num + "----lp_card_num:" + lp_card_num)
            if loc_card_num == tp_card_num and cand_fgp == fgp:
                find = True
                break
        if find:
            break
    if find:
        count = count + 1
        result.append({qry_id: qry_id, first_src_card_num: first_src_card_num, tp_card_num: tp_card_num})
        if first_src_card_num not in result_first_src_card_nums:
            result_first_src_card_nums.append(first_src_card_num)
        print("count:" + str(count) + "----qry_id:" + str(
            qry_id) + "----first_src_card_num:" + first_src_card_num + "----tp_card_num:" + tp_card_num)

# 结果进行处理
print("所有查询比中数：" + str(len(result)))
print("重复查询过滤后比中数：" + str(len(result_first_src_card_nums)))
