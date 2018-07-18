# *- coding:utf8 *-
# 兼容linux系统
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))  # 增加系统路径
from ManagerSystem.models import model
import pymysql

class databse_deal():
    def __init__(self):
        self.conn = pymysql.connect(
            host=model.cfg.host, user=model.cfg.username,
            passwd=model.cfg.password, charset=model.cfg.charset)
        self.cursor = self.conn.cursor()

    def create_database(self):
        sql = "create database if not exists {0} DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;".format(
            model.cfg.database)
        print sql
        try:
            self.cursor.execute(sql)
        except Exception, e:
            print(e)
        finally:
            self.conn_close()

    def drop_database(self):
        sql = "drop database if exists {0} ;".format(
            model.cfg.database)
        print sql
        try:
            self.cursor.execute(sql)
        except Exception, e:
            print(e)

        finally:
            self.conn_close()

    def conn_close(self):
        self.conn.close()


if __name__ == "__main__":
    db = databse_deal()
    print("start")
    '''
       运行该文件就可以在对应的数据库里生成本文件声明的所有table
       如果需要清除数据库，输入drop
       如果需要创建数据库 输入任意不包含drop的字符
       '''
    action = raw_input("create database?")
    if "drop" in action:
        db.drop_database()

    else:
        db.create_database()
        model.Base.metadata.create_all(model.mysql_engine)

    print("over")
