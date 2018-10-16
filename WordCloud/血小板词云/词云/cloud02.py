from os import path
from PIL import Image
import jieba
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
# 获得模块所在的路径的
d = path.dirname(__file__)
# Read the whole text.
text = open('细胞.txt', 'r', encoding='utf-8').read()
text +=' '.join(jieba.cut(text))
#print(text)
backgroud_Image = np.array(Image.open(path.join(d, "pic09.png")))

# 设置停用词
stopwords = set(STOPWORDS)
stopwords.add("said")

# 你可以通过 mask 参数 来设置词云形状
wc = WordCloud(background_color="white",# 设置背景颜色
               font_path='C:\Windows\Fonts\STXINGKA.TTF', # 若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
               max_words=5000,# 设置最大现实的字数
               mask=backgroud_Image,# 设置背景图片
               stopwords=stopwords,# 设置停用词
               max_font_size=50,# 设置字体最大值
               #min_font_size=10,
               random_state=100# 设置有多少种随机生成状态，即有多少种配色方案
               )
# generate word cloud
wc.generate(text)
#词频
#wc.generate_from_frequencies(text)

#改变字体颜色
image_colors = ImageColorGenerator(backgroud_Image)


# 在只设置mask的情况下,你将会得到一个拥有图片形状的词云
'''
plt.imshow(wc, interpolation="bilinear")
plt.axis("on")
plt.figure()
'''
#字体颜色为背景图片的颜色
# we could also give color_func=image_colors directly in the constructor
# 我们还可以直接在构造函数中直接给颜色
# 通过这种方式词云将会按照给定的图片颜色布局生成字体颜色策略
# 显示词云图
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.figure()


plt.imshow(backgroud_Image, cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("on")
plt.show()

