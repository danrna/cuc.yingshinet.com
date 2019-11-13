# 第十二章 分词与词云图可视化

## 第一节 词云图概述

<iframe src="/CH12/wordcloud+.htm" scrolling="yes" frameborder="0" width="100%" height="600px"></iframe>

## 第二节 D3 词云图（JSP+MySQL）

<iframe src="/CH12/english.jsp" scrolling="yes" frameborder="0" width="100%" height="600px"></iframe>

## 第三节 基于 Python Jieba 的分词实例

### 1.分词实例之 JiebaHello

```py
# encoding=utf-8
import jieba

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("【全模式】: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("【精确模式】: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print("【新词识别】: " + "/ ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print("【搜索引擎模式】: " + "/ ".join(seg_list))
```

### 2.添加词典

```py
#ecoding=utf-8
import jieba

jieba.load_userdict("jiebaDict.txt")
words=jieba.cut("他来到了网易杭研大厦")
print("/ ".join(words))
```

### 3.词性标注

```py
import jieba.posseg as pseg
words=pseg.cut("中国国家领导人在开会")
for key in words:
    print(key.word,key.flag)
```

## 第四节 影视剧小说词云图实例分析

### 1.添加的人名词典

```txt
侯亮平 1 n
沙瑞金 1 n
李达康 1 n
高育良 1 n
祁同伟 1 n
陆亦可 1 n
高小琴 1 n
吴惠芬 1 n
刘新建 1 n
陈岩石 1 n
季昌明 1 n
赵瑞龙 1 n
郑西坡 1 n
钟小艾 1 n
赵东来 1 n
蔡成功 1 n
欧阳菁 1 n
丁义珍 1 n
程度 1 n
陈海 1 n
郑胜利 1 n
王文革 1 n
```

### 2.Python分词程序

```py
import jieba

with open('renmin.txt', 'r') as f:
    renmin=f.read()

jieba.load_userdict("renminDict.txt")  #添加词典
seg_list = jieba.cut(renmin, cut_all=False) #分词
print("【精确模式】: " + "/ ".join(seg_list))
tf = {}
for seg in seg_list:
        if seg in tf:     # 如果该键存在于集合tf的对象中，则该键所属对象值加1
            tf[seg] +=1
        else:		      #否则，生成新词的键值对，初始值为1
            tf[seg] = 1

ci = list(tf.keys())	#将分词结果中的所有键值，即词语，放置在一个列表
with open('stopword.txt', 'r') as ft:
    stopword=ft.read()
for seg in ci:	#逐个判断是否停用词，及对词语长度进行处理
    if tf[seg]<20 or len(seg)<2 or seg in stopword or '一'in seg:
        tf.pop(seg)	#若属停用词，则删去该键值对

		
#过滤后的词语和词频分别存入列表ci和num中，并将data声明为列表，以存储键值对		
ci, num, data = list(tf.keys()), list(tf.values()),[]	

for i in range(len(tf)):
    data.append((num[i],ci[i]))	#逐个将键值对存入data中
data.sort()	#升序排列
data.reverse()	#逆序，得到所需的降序排列
f = open("result.txt", "w")
for i in range(len(data)):
    f.write("[\""+data[i][1]+"\","+str(data[i][0])+"],")	#以下文词云API所需数据格式存入文件
f.close()
```

### 3.Echart2词云图

<iframe src="/CH12/renminWC.htm" scrolling="yes" frameborder="0" width="100%" height="600px"></iframe>

## 第五节 三维动态词云

### 1.三维词云图

<iframe src="/CH12/wordcloud3D.htm" scrolling="yes" frameborder="0" width="100%" height="600px"></iframe>

### 2.影视搜图片三维词云

<iframe src="http://movies.we-yun.com/" scrolling="yes" frameborder="0" width="100%" height="600px"></iframe>
