
'''读取配置文件'''
import  os,configparser
class ReadConfig():
    #类内部定义参数
    db_='database'
    host_='host'
    port_='port'
    user_='user'
    passwd_='passwd'

    #定义参数
    host=''
    port=''
    user=''
    passwd=''
    database=''
    '''构造，读取配置文件'''
    def __init__(self):
        #目录
        curPath=os.path.dirname(os.path.realpath(__file__))
        configPath=os.path.join(curPath,"config.ini")
        #文件
        conf=configparser.ConfigParser()
        conf.read(configPath)
        #遍历配置文件中的参数
        self.host=conf.get(self.db_,self.host_)
        self.port=conf.get(self.db_,self.port_)
        self.user=conf.get(self.db_,self.user_)
        self.passwd=conf.get(self.db_,self.passwd_)
        self.database=conf.get(self.db_,self.db_)
if __name__ == '__main__':
    a=ReadConfig()
    print(a.host)