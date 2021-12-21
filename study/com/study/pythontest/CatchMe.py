
'''爬取百度热搜'''
import urllib.request
import time
import os
import  re
from bs4 import BeautifulSoup
#from 包名.文件名 import 类名
from study.com.study.pythontest.dao.OperateRsDao import OperateRsDao
from study.com.study.pythontest.tools.uuid_tools import uuid_tools
from study.com.study.pythontest.vo.RsBean import RsBean


class CatchMe:
    catchUrl="https://top.baidu.com/board?tab=realtime&sa=fyb_realtime_31065"
    text=''
    today=''
    writePosition='d:\\bdrs\\'
    bmcode='utf-8'
    fileName=''
    '''构造函数'''
    def __init__(self,catchUrl,text,today,writePosition,bmcode):
        self.catchUrl=catchUrl if  catchUrl else self.catchUrl
        self.text=text
        self.today=today
        self.writePosition=writePosition if writePosition else self.writePosition
        self.bmcode=bmcode if bmcode else self.bmcode
    '''读取页面'''
    def readhtml(self,catchUrl):
        catchUrl=self.catchUrl if not catchUrl else catchUrl
        response=urllib.request.urlopen(catchUrl)
        text=response.read().decode(self.bmcode)
        return text
    '''生成时间'''
    def createTime(self):
        # 格式化成2016-03-20 11:45:39形式
        return time.strftime("%Y%m%d%H", time.localtime())
    '''写入文件'''
    def write2file(self,text):
        fileName=self.writePosition+self.createTime()+'.txt'
        self.fileName=fileName
        print(fileName)
        #判断路径，不存在生成
        if not os.path.exists(self.writePosition):
            os.mkdir(self.writePosition )
        if os.path.exists(fileName):
            uuid_tools().printlog('已经存在：{}'.format(fileName))
            return self.fileName
        mode='a' if os.path.exists(fileName) else 'w'

        with open(fileName,mode,encoding=self.bmcode) as f:
            f.write(text)
        print("写入{} 完成".format(fileName))
        return self.fileName
    '''去掉标签'''
    def removeBq(self,content):
        pat=re.compile('>(.*?)<')
        str=''.join(pat.findall(content))
        str=str.replace(' 查看更多&gt; ','')
        return str
    '''输出内容'''
    def printContent(self, o,class_name):
        print(self.removeBq(str(o.find(class_=class_name))))

    '''返回结果'''
    def getContent(self, o,class_name):
        return (self.removeBq(str(o.find(class_=class_name))))
    '''获取文件的名字'''
    def cutfilename(self,fileName):
        #mystr='d:\\bdrs\\2021122010.txt'
        return ( re.search(r'(\d+)',fileName).group() )
    '''清空表'''
    def clearBefore(self,daoOper,rs_shijian):
        sql="delete from bdrs_one where rs_shijian=%s or rs_shijian=%s or rs_shijian is null"
        val=(rs_shijian,'')
        daoOper.deletetable(sql,val)
        print("清空完成")
    '''插入数据'''
    def insertData(self,daoOper,k,rs):
        uuidtools=uuid_tools()
        sql='insert into bdrs_one(id,shun_xu,biao_ti,tu_pian,miao_shu,reshou_zhishu,insert_time,rs_shijian)' \
            'values(%s,%s,%s,%s,%s,%s,now(),%s)';
        val=(
            uuidtools.getuuid(),
            self.getContent(k,rs.sx),
            self.getContent(k,rs.bt),
            '',
            self.getContent(k,rs.ms),
            self.getContent(k,rs.rszs),
            rs.rs_shijian)
        daoOper.insert(sql,val)
        print("insertData-over")
    '''读取文件'''
    def readFile(self,fileName):
        #fileName='d:\\bdrs\\2021122010.txt'
        jt=open(fileName,'r',encoding=self.bmcode)
        try:
            content=jt.read()
            soup=BeautifulSoup(content,"html.parser")
            rs=RsBean()
            daoOper=OperateRsDao()
            rs_shijian=self.cutfilename(fileName)
            #先清空
            self.clearBefore(daoOper,rs_shijian)
            #读取文件
            for k in soup.find_all('div',class_=rs.alldiv):
                #插入数据
                rs.rs_shijian=rs_shijian
                self.insertData(daoOper,k,rs)
        except  Exception as e:
            print('error:'+str(e))
    '''测试获取某个片段'''
    def readFilePd(self,fileName):
        #fileName='d:\\bdrs\\2021122010.txt'
        jt=open(fileName,'r',encoding=self.bmcode)
        try:
            content=jt.read()
            soup=BeautifulSoup(content,"html.parser")
            rs=RsBean()
            for k in soup.find_all('div',class_=rs.alldiv):
                print( str(k))
                # self.printContent(k,rs.sx)
                # self.printContent(k,rs.bt)
                # self.printContent(k,rs.ms)
                # self.printContent(k,rs.rszs)
        except  Exception as e:
            print('error:'+str(e))

'''定格的main函数'''
if __name__ == '__main__':
    a=CatchMe('','','','','')
    # print(a.bmcode+",读取页面："+a.catchUrl)
    # a.text=a.readhtml('')
    # print("写入文件：")
    # a.write2file(a.text)
    a.fileName=a.write2file(a.readhtml(''))
    a.readFile(a.fileName)