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