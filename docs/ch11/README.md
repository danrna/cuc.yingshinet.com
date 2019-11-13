# 第十一章 数据可视化之数据获取

## 第一节 Python爬虫基础

### 1.请求获取URL网页数据

```py
import requests
url='http://music.163.com/#/artist?id=6697'
r=requests.get(url).text
print(r)

r = requests.post("http://httpbin.org/post")
r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get")
```

### 2.请求一个W3C页面数据

```py
import requests

keyword ='html_image'
try:
    keyword={'f':keyword}
    r = requests.get("http://www.w3school.com.cn/tiy/t.asp",params = keyword)
    print(r.url)
    print(r.text)
except:
    print("error")
```

### 3.请求图片数据

```py
import requests

keyword ='html_image'
print(keyword)
try:
    keyword={'f':keyword}
    r = requests.get("http://www.w3school.com.cn//i/eg_mouse.jpg")
    print(r.url)
    print(r.content)
    f = open('w3c.jpg', 'wb')
    f.write(r.content)
    f.close()
except:
    print("error")
```

## 第二节 解析数据

### 1.使用BS4解析数据

```py
from bs4 import BeautifulSoup
import requests
try:
    r=requests.get("http://www.w3school.com.cn/tiy/t.asp?f=jseg_text")
    soup = BeautifulSoup(r.text,'html.parser')
    href=soup.find_all('a')
    print(href)
except:
    print("error")
```

### 2.正则表达式解析数据

```py
import re
str='data=["中国","美国","日本","英国"];city=["广州","北京","上海","深圳"];'
result = re.match(r'data=(.*?);',str)
print(result.group(1))
```

## 第三节 数据存储与知识图谱

### 1.数据存入TXT文件

```py
data=["名称最新价涨跌幅",
      "永安行 38.66 43.99%",
      "秦港股份 3.71 10.09%",
      "中船科技 18.54 10.03%"]
with open('data.txt','w+',encoding='utf-8') as f:
	for d in data:
		f.writelines(d+'\n')
```

### 2.数据存入MySQL

```py
import pymysql

data=[['永安行', '38.66', '43.99%'],
      ['秦港股份', '3.71', '10.09%'],
      ['中船科技', '18.54', '10.03%']]

# pymysql.connect(数据库url,用户名,密码,数据库名 )
db = pymysql.connect("localhost", "root", "123456", "SpiderDB", charset = 'utf8')
cursor = db.cursor()
try:
    for d in data:
        cursor.execute("INSERT INTO stock(name,price,rise) VALUES(%s,%s,%s)", (d[0], d[1], d[2]))
        print("ok")
        db.commit()
except:
    db.rollback()
db.close()
```

### 3.爬取WikiPedia数据

```py
# -*- coding: utf-8 -*
import requests
from bs4 import BeautifulSoup
import json
import re
import queue
class leaf:
    def __init__(self,name,brief,lid,children,url):
        self.name=name
        self.brief=brief
        self.id=lid
        self.children=children
        self.url=url

keywordDict=[]
nodes=[]
links=[]
urllist=queue.Queue()
depth=3
leafMax=3
baseUrl="https://en.wikipedia.org"
Default_Header={
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding':'gzip, deflate, br',
'accept-language':'zh-CN,zh;q=0.8',
'cache-control':'max-age=0',
'cookie':'CP=H2; GeoIP=JP:13:Tokyo:35.64:139.77:v4; WMF-Last-Access=12-Aug-2017; WMF-Last-Access-Global=12-Aug-2017; TBLkisOn=0',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
}
_session = requests.session()
#requests.adapters.DEFAULT_RETRIES = 3
_session.headers.update(Default_Header)
'''_session.keep_alive = False'''
def addKeyword(word):
    if word in keywordDict:
        for i in range(0,len(keywordDict)):
            if word==keywordDict[i]:
                return i
    else:
        keywordDict.append(word)
        return len(keywordDict)-1

def isNew(id):
    if id<len(keywordDict)-1:
        return False
    else:
        return True

def getHTMLText(url):
    try:
        r = _session.get(url)
        r.raise_for_status()
        r.encoding = "UTF-8"
        return r.text
    except:
        return ""

def wideLeaf(html,level,fid):
    try:
        soup = BeautifulSoup(html, 'lxml')
        name = str(soup.find('h1', attrs={'id': 'firstHeading'}).string)
        lid = addKeyword(name)
        print(name + str(len(keywordDict)) + str(isNew(lid)))
        if isNew(lid):
            nodes.append({"name": name, "group": lid})
            contentHtml = soup.find('div', attrs={'class': 'mw-parser-output'})
            birefHtml = contentHtml.find_all('p', recursive=False)
            count = 0
            for tag in birefHtml:
                strings = re.findall(r'>.*?<', str(tag))
                sentence = re.sub(r'[>|<]', '', ''.join(strings))
                # 简介终止
                if sentence == '':
                    break
                for a in tag.find_all('a', href=re.compile('/wiki/')):
                    urllist.put([a.attrs['href'], level + 1, lid])
                    count += 1
                    if count > leafMax: break

        if fid>-1:
            links.append({"source":fid,"target":lid,"value":1})
    except Exception as e:
        print(e)
        return
#0:url 1:level 2:fatherId
def wideWiki(start_url,dep):
    wideLeaf(getHTMLText(start_url),1,-1)
    while(True):
        if urllist.empty():
            break
        leaf=urllist.get()
        print(str(leaf)+str(urllist.qsize()))
        if leaf[1]==dep+1:
            break
        wideLeaf(getHTMLText(baseUrl +leaf[0]),leaf[1],leaf[2])




def main():
    keyword = 'JavaScript'
    start_url = 'https://en.wikipedia.org/wiki/' + keyword
    wideWiki(start_url,depth)
    with open('wikidata.json','w+',encoding='utf-8') as f:
        f.write("nodes="+json.dumps(nodes,ensure_ascii=False))
        f.write(";\nlinks="+json.dumps(links,ensure_ascii=False))

if __name__=="__main__":
    main()
    pass
```

### 4.WikiPedia词条知识图谱

<iframe src="/CH11/wikiGraph.htm" scrolling="yes" frameborder="0" width="100%" height="600px"></iframe>
