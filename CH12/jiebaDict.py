#ecoding=utf-8
import jieba

jieba.load_userdict("jiebaDict.txt")
words=jieba.cut("他来到了网易杭研大厦")
print("/ ".join(words))
