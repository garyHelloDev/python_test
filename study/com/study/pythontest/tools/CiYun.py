import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

class CiYun:
    def __init__(self):
        pass
    '''词云显示'''
    def showImage(self,mystr):
        wordlist_after_jieba = jieba.cut(mystr, cut_all = True)
        wl_space_split = " ".join(wordlist_after_jieba)
        font = r"C:\Windows\Fonts\simfang.ttf"
        my_wordcloud = WordCloud(width=1000,
                                 height=700,font_path=font,background_color='white').generate(wl_space_split)
        plt.imshow(my_wordcloud)
        plt.axis("off")
        plt.show()
        '''读取文件'''
    def readfile(self):
        # 从外部.txt文件中读取大段文本，存入变量txt中
        f = open('乡村振兴.txt',encoding='utf-8')
        txt = f.read()
        # 构建词云对象w，设置词云图片宽、高、字体、背景颜色等参数
        font = r"C:\Windows\Fonts\simfang.ttf"
        w =WordCloud(width=1000,
                                height=700,
                                background_color='white',
                                font_path=font)
        # 将txt变量传入w的generate()方法，给词云输入文字
        w.generate(txt)

        # 将词云图片导出到当前文件夹
        w.to_file('output3-sentence.png')
if __name__ == '__main__':
    CiYun().readfile()