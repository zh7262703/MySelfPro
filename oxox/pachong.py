# -*- coding: utf-8 -*-
# 导入库
from urllib import request
#内容的抓取操作
from bs4 import BeautifulSoup

# 请求
response = request.urlopen("http://www.baidu.com/")

# 解码
html_content = response.read().decode('utf-8')

beditor=BeautifulSoup(html_content,'html.parser')

myh1=beditor.find('h1')  #find方法只能找到一个

myh2=beditor.findAll('h1') #findall方法查找所有的

# 输出1
print(myh1.string)

#输出2
for i in myh2:
    print(i.string)

