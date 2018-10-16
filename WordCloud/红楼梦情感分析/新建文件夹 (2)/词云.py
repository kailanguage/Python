# coding=utf-8

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

txt1 = open('C:/Users/chenkailang/Desktop/hongloumeng/上卷.txt', 'r', encoding='utf8').read()    # word.txt，随便放点中文文章
words_ls = jieba.cut(txt1, cut_all=True)
words_split = " ".join(words_ls)

wc = WordCloud()    # 字体这里有个坑，一定要设这个参数。否则会显示一堆小方框wc.font_path="simhei.ttf"   # 黑体
my_wordcloud = wc.generate(words_split)
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

wc.to_file('./zzz.png') # 保存图片文件
