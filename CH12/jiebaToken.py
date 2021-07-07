import jieba.posseg as pseg
words=pseg.cut("中国国家领导人在开会")
for key in words:
    print(key.word,key.flag)