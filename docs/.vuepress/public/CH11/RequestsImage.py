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