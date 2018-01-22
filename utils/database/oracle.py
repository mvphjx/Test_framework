from utils.config import Config

oracle_url = Config().get("oracle_url")
oracle_username = Config().get("oracle_username")
oracle_password = Config().get("oracle_password")
import cx_Oracle
#操作oracle demo



connection = cx_Oracle.connect(oracle_username, oracle_password, oracle_url)  # 创建连接
cursor = connection.cursor()  # 创建cursor
sql = 'select * from USER_VIEW'
cursor.execute(sql)  # 执行sql 语句
for values in cursor:
    print("Row Value:", values)




