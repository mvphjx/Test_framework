from utils.config import Config

import cx_Oracle


# 操作oracle demo

class OracleConnection:
    def __init__(self):
        self.oracle_url = Config().get("oracle_url")
        self.oracle_username = Config().get("oracle_username")
        self.oracle_password = Config().get("oracle_password")
        self.connection = cx_Oracle.connect(self.oracle_username, self.oracle_password, self.oracle_url)  # 创建连接

    def get_connection(self):
        return self.connection