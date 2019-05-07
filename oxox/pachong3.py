#coding = utf-8
from urllib import request
import urllib
#内容的抓取操作
from bs4 import BeautifulSoup

import re

#数据库操作
import oracleTest

import threading
from time import ctime,sleep

#所有连接
counttimes = 0

listUrls = []

#线程结束标记
endflag = 0

def getlistHrefCout(func):
   while 1!= 0:
       try:
          print("current count Times:"+str(counttimes))
          sleep(1)
       except Exception as err:
           print(err)

def getHtml(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    page1 = urllib.request.Request(url, headers=headers)
    page = request.urlopen(page1, timeout=100)
    html = page.read().decode('gbk', 'ignore')
    page.close()
    return html

def IsHaveUrl(url):
    for k in listUrls:
        if k == url:
            return 1
    return 0


def getListHref(url, cout):
    # page = request.urlopen(url,timeout=1000)
    html =getHtml(url)
    beditor = BeautifulSoup(html, 'html.parser')
    content = beditor.find(name='div', class_='content-wrap')
    cout += 1

    counttimes = cout
    print(counttimes)
    if content!=None:
       print(content.get_text())
    # if content!=None:
    #     #插入数据库
    #     param = [url, content.get_text()]
    #     oracleTest.ExecuteSQL("insert into T_PACHONG(url,div)values(:url,:content)",param)


    for k in beditor.find_all('a'):
        try:
           str1 = k['href']
           if str1 != '' and IsHaveUrl(str1) == 0 :
              if re.match(r'^https?:/{2}\w.+$', str1) == False:
                  str1="https://www.haodf.com" +str1
              print(str1)
              listUrls.append(str1)
              getListHref(str1, counttimes)
        except Exception as err:
              print(err)
    endflag = 1
    print(counttimes)



#threads = []
#t1 = threading.Thread(target=getlistHrefCout,args=(u'连接数量',))
#threads.append(t1)
#t1.setDaemon(True)
#t1.start()
# for t in threads:
#     t.setDaemon(True)
#     t.start()


    # reg = 'href="(.+?\.jpg)"'
getListHref("https://www.haodf.com/jibing/list.htm",counttimes)


#http://www.jk.cn/hl/detail/3589279

# url2 = "https://www.haodf.com/jibing/list.htm"
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
# page1 = urllib.request.Request(url2,headers=headers)
# page = request.urlopen(page1,timeout=100)
# html = page.read().decode('gbk', 'ignore')
# page.close()
# print(html)
