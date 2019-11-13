import requests

keyword ='html_image'
try:
    keyword={'f':keyword}
    r = requests.get("http://www.w3school.com.cn/tiy/t.asp",params = keyword)
    print(r.url)
    print(r.text)
except:
    print("error")