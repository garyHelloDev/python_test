
import  uuid,logging
'''生成UUID'''
class uuid_tools():
    def __init__(self):
        pass
    '''uuid1包括了mac的使用，保证唯一，Uuid4有一定可计算出来的重复'''
    def getuuid(self):
        str1=uuid.uuid1()
        str1=str(str1).replace('-','')
        return str1
    '''打印日志'''
    def printlog(self,loginfo):
        logging.basicConfig(level=logging.INFO)
        logging.info(loginfo)
if __name__ == '__main__':
    u=uuid_tools()
    print(u.getuuid())