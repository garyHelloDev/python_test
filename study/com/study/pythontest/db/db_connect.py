

import pymysql

from study.com.study.pythontest.db.ReadConfig import ReadConfig
from study.com.study.pythontest.tools.CiYun import CiYun

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
        self.db=pymysql.connect(host=self.host,port=3306,user=self.user,passwd=self.passwd,db=self.database)
        #创建游标
        self.cursor=self.db.cursor()
        #print("打开连接成功")
    #关闭
    def close(self):
        self.cursor.close()
        self.db.close()
        #print("close连接成功")
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
            result=self.cursor.fetchall()
        except Exception as e:
            print("Execute failure!",str(e))
        self.close()
        return result

if __name__ == '__main__':
    a=db_connect()
    sql='select id,shun_xu,biao_ti,miao_shu,reshou_zhishu,insert_time,rs_shijian from bdrs_one order by rs_shijian desc,shun_xu asc '
    result=a.select(sql)
    jieguo=''
    for m in result:
        print(m)
        jieguo+=m[2]
    #根据title做词云
    CiYun().showImage(jieguo)