from urllib.request import urlopen
url="http://www.baidu.com"
resp= urlopen(url)  #用urlopen拿出网站
# print(resp.read().decode("UTF-8"))
with open("mybaidu.html",mode="w",encoding="utf-8") as f:     #建一个空文件夹，名为f
    f.write(resp.read().decode("UTF-8"))   #write 往文件里写内容：  read读取网站本身

    #decode：爬来的乱码转中文    encoding :保存时