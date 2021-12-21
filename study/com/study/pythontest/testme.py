import time
from tqdm import  tqdm ,trange
import uuid,re
import logging

from study.com.study.pythontest.tools.uuid_tools import uuid_tools

'''
测试 ,进度条
'''
def test1():
    for i in trange(100):
        time.sleep(0.05)

def test2():
    dic = ['a', 'b', 'c', 'd', 'e']
    pbar = tqdm(dic)
    for i in pbar:
        pbar.set_description('Processing '+i)
        time.sleep(0.5)
def testuuid():
    print(uuid.uuid4())
    '''截取斜杠和点的文件名称'''
def cutfilename():
    mystr='d:\\bdrs\\2021122010.txt'
    print( re.search(r'(\d+).txt',mystr).group() )
if __name__ == '__main__':
    #cutfilename()
    uuid_tools().printlog("3333sdf阿萨德飞")