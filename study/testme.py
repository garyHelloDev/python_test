import time
from tqdm import  tqdm ,trange

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
        time.sleep(0.2)
if __name__ == '__main__':
    test2()