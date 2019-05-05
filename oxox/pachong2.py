#coding = utf-8
from urllib import request
import re

def getHtml(url):
    page = request.urlopen(url,timeout=1000)
    html = page.read().decode('utf-8',"ignore")
    return html

def getImg(html):
    #reg = 'src="(.+?\.jpg)" alt='
    reg = 'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)

    x = 0
    errlist = []
    for imgurl in imglist:
        try:
           request.urlretrieve(imgurl, '%s.jpg' % x)
           x+=1
        except Exception as err:
           errlist.append(err)
           print(err)

   # print(errlist)
    return imglist

html = getHtml("https://www.pictoa.com/albums/cock-crush-717890.html")
#"http://pic.yxdown.com/list/0_0_1.html"
imgList=getImg(html)
for imgurl in imgList:
   print(imgurl)

