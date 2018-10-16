# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
import jieba
import jieba.analyse

output = open('words.csv', 'a')
output.write('词语,词频,词权\n')
stopkeyword = [line.strip() for line in open('stop.txt').readlines()]  # 将停止词文件保存到列表
text = open(r"上卷.txt", "r").read()  # 导入需要计算的内容
zidian = {}
fenci = jieba.cut_for_search(text)
for fc in fenci:
    if fc in zidian:
        zidian[fc] += 1
    else:
        # zidian.setdefault(fc,1)   #字典中如果不存在键，就加入键，键值设置为1
        zidian[fc] = 1
tfidf = jieba.analyse.extract_tags(text, topK=30, withWeight=True)

for word_weight in tfidf:
    if word_weight in stopkeyword:
        pass
    else:  # 不存在的话就输出
        print word_weight[0], zidian.get(word_weight[0], 'not found'), str(int(word_weight[1] * 100)) + '%'
        output.write('%s,%s,%s\n' % (
        word_weight[0], zidian.get(word_weight[0], 'not found'), str(int(word_weight[1] * 100)) + '%'))
