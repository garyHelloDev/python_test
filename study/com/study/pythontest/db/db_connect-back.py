

import pymysql

from study.com.study.pythontest.db.ReadConfig import ReadConfig

'''连接数据库'''
class db_connect():
    b=ReadConfig()
    def __init__(self,
                 host=b.host,
                 port=b.port,
                 user=b.user,
                 passwd=b.passwd,
                 database=b.database
                 ):
        self.host=host
        self.port=port
        self.user=user
        self.passwd=passwd
        self.database=database
    '''打开连接'''
    def open(self):
        db=pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,db=self.database)
        #创建游标
        self.cursor=self.db.cursor()
    #关闭
    def close(self):
        self.cursor.close()
        self.db.close()
    def execute(self,sql,list=[]):
        try:
            self.open()
            self.cursor.execute(sql,list)
            self.db.commit()
            print("execute successfully!")
        except Exception as e:
            self.db.rollback()
            print("Execute failure!",str(e))
        self.close()
    '''执行，无参'''
    def executeNoParam(self,sql):
        try:
            self.open()
            self.cursor.execute(sql)
            self.db.commit()
            print("execute successfully!")
        except Exception as e:
            self.db.rollback()
            print("Execute failure!",str(e))
        self.close()
    '''执行查询'''
    def select(self,sql):
        try:
            self.open()
            self.cursor.execute(sql)
            result=self.cursor.fetcheall()
        except Exception as e:
            print("Execute failure!",str(e))
        self.close()
        return result

