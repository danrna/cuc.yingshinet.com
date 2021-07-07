data=["名称最新价涨跌幅",
      "永安行 38.66 43.99%",
      "秦港股份 3.71 10.09%",
      "中船科技 18.54 10.03%"]
with open('data.txt','w+',encoding='utf-8') as f:
	for d in data:
		f.writelines(d+'\n')
