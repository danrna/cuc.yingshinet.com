# -*- coding: utf-8 -*
import requests
from bs4 import BeautifulSoup
import json
import re

class leaf:
    def __init__(self,name,brief,lid,children):
        self.name=name
        self.brief=brief
        self.id=lid
        self.children=children

keywordDict=[]
depth=10
#词条的相对路径的相同部分
baseUrl='https://en.wikipedia.org'
#添加新词条
def addKeyword(word):
    if word in keywordDict:
        for i in range(0,len(keywordDict)):
            if word==keywordDict[i]:
                return i
    else:
        keywordDict.append(word)
        return len(keywordDict)-1
#判断词条是否存在
def isNew(id):
    if id<len(keywordDict)-1:
        return False
    else:
        return True

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = "UTF-8"
        #print(r.text)
        return r.text
    except:
        return ""

def getLeaf(html,level):
    name=''
    brief=''
    lid=''
    children=[]
    urllist=[]
    try:
        soup = BeautifulSoup(html, 'lxml')
	    #获取词条标题部分
        print(soup.find('h1', attrs={'id': 'firstHeading'}))
        name = str(soup.find('h1', attrs={'id': 'firstHeading'}).string)
        print(name +' '+ str(len(keywordDict)))
	    #存储词条
        lid = addKeyword(name)
        print(lid)
	    #获取简介部分
        contentHtml = soup.find('div', attrs={'class': 'mw-parser-output'})
        briefHtml = contentHtml.find_all('p', recursive=False)
        for tag in briefHtml:
	    #提取p标签中纯文字部分
            strings = re.findall(r'>.*?<', str(tag))
            sentence = re.sub(r'[>|<]', '', ''.join(strings))
            # 简介到第一个内容为空的p标签终止
            if sentence == '':
                break
	    #对内容进行拼接
            brief += sentence + '<br>'
            print(brief)
            #print(tag.find_all('a',href=re.compile('/wiki/'))

            for a in tag.find_all('a',href=re.compile('/wiki/')):
                print(a)
                urllist.append(a.attrs['href'])
                if level >= depth or not isNew(lid):
                    #将类字典化方便转换为JSON格式
                    return leaf(name, brief, lid, children, "").__dict__

            for link in urllist:
                #进入关联词条页面递归继续上述操作
                children.append(getLeaf(getHTMLText(baseUrl + link), level + 1))
                return leaf(name, brief, lid, children).__dict__
    except Exception as e:
        print(e)
    return


def main():
    keyword = 'JavaScript'
    start_url = 'https://en.wikipedia.org/wiki/' + keyword
	print('---------------------------------------------------------------------------------')
    print(start_url)
    root=getLeaf(getHTMLText(start_url),1)
    with open('datafull.js','w+',encoding='utf-8') as f:
        f.write("data="+json.dumps(root,ensure_ascii=False))
        f.write(";\ndict="+json.dumps(keywordDict,ensure_ascii=False))
#主函数调用main()方法执行爬取操作
if __name__=="__main__":
    main()
    pass



