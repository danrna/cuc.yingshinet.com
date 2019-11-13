import requests
url='http://music.163.com/#/artist?id=6697'
r=requests.get(url).text
print(r)

r = requests.post("http://httpbin.org/post")
r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get")
