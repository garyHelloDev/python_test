from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open("野性的呼唤.txt", encoding="utf-8") as file:
    word_cloud = WordCloud().generate(file.read())
    plt.figure()      # 创建一个图形实例
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")  # 不显示坐标轴
    plt.show()