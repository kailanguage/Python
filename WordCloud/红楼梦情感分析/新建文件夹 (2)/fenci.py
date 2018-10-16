import jieba
article = open("C:/Users/chenkailang/Desktop/hongloumeng/上卷.txt", "rb")
words = jieba.cut(article, cut_all = False)
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

freq_word = []
for word, freq in word_freq.items():
    freq_word.append((word, freq))
freq_word.sort(key = lambda x: x[1], reverse = True)

max_number = int(raw_input(u"需要前多少位高频词？ "))

for word, freq in freq_word[: max_number]:
    print (word,freq)
