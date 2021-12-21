
from study.com.study.pythontest.db.db_connect import db_connect
import logging

from study.com.study.pythontest.tools.uuid_tools import uuid_tools

'''操作数据库'''
class OperateRsDao():
    logging=logging.getLogger()
    db=db_connect()
    def __init__(self):
        pass
        #self.initDatabase()
    '''初始化数据库和表'''
    def initDatabase(self):
        sql='create database if not exists bdrs ; use bdrs; create table if not exists bdrs_one( id varchar(50) not null  ,shun_xu varchar(50) ,biao_ti varchar(50) ,tu_pian varchar(50) ,miao_shu varchar(50) ,reshou_zhishu int );'
        db_connect().executeNoParam(sql)
        uuid_tools().printlog('初始化数据库和表---完成')
        '''插入'''
    def insert(self,sql,list=[]):
        db_connect().execute(sql,list)
        logging.info('insert表---完成')
    def deletetable(self,sql,list=[]):
        db_connect().execute(sql,list)
        logging.info('deletetable---完成')
if __name__ == '__main__':
    a=OperateRsDao()
    sql="delete from bdrs_one where rs_shijian=%s or rs_shijian=%s or rs_shijian is null"
    val=('2021122108','')
    a.deletetable(sql,val)
