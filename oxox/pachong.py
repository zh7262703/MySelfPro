# -*- coding: utf-8 -*-
# 导入库
from urllib import request

#内容的抓取操作
from bs4 import BeautifulSoup

# 请求

url1 = "https://www.google.com/search?q=she-ra+sexy+pic"
url2 = "&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjmsOeK74PiAhUBna0KHYugCFkQ_AUIDigB&biw=1569&bih=731"

response = request.urlopen("http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=she-ra",timeout=10)
print(type(response))
# 解码
html_content = response.read().decode('utf-8',"ignore")


beditor=BeautifulSoup(html_content,'html.parser')

myh1 = beditor.find('a')  #find方法只能找到一个

myh2 = beditor.findAll('a') #findall方法查找所有的

# 输出1
print(myh1.string)

#输出2
for i in myh2:
    print(i.string)

