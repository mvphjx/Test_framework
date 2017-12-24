import cx_Oracle
#操作oracle demo
connection = cx_Oracle.connect('test', 'test', "localhost/orcl")  # 创建连接
cursor = connection.cursor()  # 创建cursor
sql = 'select * from STUDENT'
cursor.execute(sql)  # 执行sql 语句
for value1, value2 in cursor:
    print("Values:", value1, value2)
