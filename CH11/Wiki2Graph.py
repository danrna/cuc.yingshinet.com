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