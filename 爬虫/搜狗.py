import requests

content = input('请输入你要检索的内容: ')
url = f"https://www.sogou.com/web?query={content}"

# 关键是添加这一段，模拟真实浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

resp = requests.get(url, headers=headers)
print(resp.text)