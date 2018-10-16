import jieba

excludes = {'什么','一个','我们','那里','你们','如今','说道','知道','起来','姑娘','这里','出来','他们','众人','自己','一面','太太','只见','怎么','两个','没有','不是','不知','这个','听见','这样','进来','咱们','告诉','就是','东西','回来','只是','大家','只得','这些','不敢','出去','所以','不过','的话','不好','一时','不能','过来','心里','如此','今日','银子','几个','答应','二人','还有','只管','这么','说话','一回','那边','这话','外头','打发','自然','今儿','罢了','屋里','那些','听说','如何','问道','看见'}

text = open("下卷.txt","r",encoding = 'utf-8').read()

words = jieba.cut(text)
counts = {}
for word in words :
    if len(word) ==1:
            continue
    elif word == "林黛玉":
	    rword = "黛玉"
    elif word == "老太太":
	    rword = "贾母"
    else:
            counts[word]=counts.get(word,0) +1
for word in excludes:
    del(counts[word])
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
print("红楼梦后四十回分词统计词频的结果:")
print("词汇\t\t频率")
print("")
for i in range(100):
    word,count =items[i]
    print("{}\t\t{}".format(word,count))
