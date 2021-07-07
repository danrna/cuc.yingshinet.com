import re
str='data=["中国","美国","日本","英国"];city=["广州","北京","上海","深圳"];'
result = re.match(r'data=(.*?);',str)
print(result.group(1))