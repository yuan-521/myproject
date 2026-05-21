import requests

url = "https://fanyi.baidu.com/sug"

hehe = {
    "kw": input("请输入一个单词")
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}
resp = requests.post(url, data=hehe)
print(resp.json())