import requests

url="http://www.baidu.com"
a=requests.get(url)
a.encoding="utf-8"
print(a.text)  #text  拿到页面源代码




#