from bs4 import BeautifulSoup
import requests
try:
    r=requests.get("http://www.w3school.com.cn/tiy/t.asp?f=jseg_text")
    soup = BeautifulSoup(r.text,'html.parser')
    href=soup.find_all('a')
    print(href)
except:
    print("error")


