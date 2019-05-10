# -*- coding: GBK -*-

import json
import urllib
import sys
from resty import PathDispatcher
from wsgiref.simple_server import make_server
import oracleTest

#=urllib.parse.unquote_to_bytes(path).decode('iso-8859-1')

# 定义函数，参数是函数的两个参数，都是python本身定义的，默认就行了。
def application(environ, start_response):
    # 定义文件请求的类型和当前请求成功的code
    start_response('200 OK', [('Content-Type', 'text/html')])
    # environ是当前请求的所有数据，包括Header和URL，body，这里只涉及到get
    # 获取当前get请求的所有数据，返回是string类型
    params = urllib.parse.parse_qs(environ['QUERY_STRING'])
    # 获取get中key为name的值
    name = params.get('name', [''])[0]
    no = params.get('no', [''])[0]

    # 组成一个数组，数组中只有一个字典
    dic = {'name': name, 'no': no}
    return [json.dumps(dic)]

def hello_world(environ, start_response):
    start_response('200 OK', [('Content-Type','text/html;chartset=utf-8')])
    strval = "hello word 大口径的空间!"    #% (environ['PATH_INFO'].encode('iso-8859-1').decode('utf8')[1:] or 'web')
    yield strval

def GetUsers(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html;chartset=utf-8')])
    params = urllib.parse.parse_qs(environ['QUERY_STRING'])
    username = params.get('username', [''])[0]
    sql = "select user_id,user_name,user_num,gender_code from t_userinfo where user_name like '%" + username + "%'"
    rs = oracleTest.GetDataSet(sql)
    return [json.dumps(rs)]


#print(sys.getdefaultencoding())

if __name__ == "__main__":
    port = 5088
    dispatcher = PathDispatcher()
    dispatcher.register('GET', '/hello', hello_world)
    dispatcher.register('GET', '/userinfo', GetUsers)
    #dispatcher.register('GET', '/localtime', localtime)
    httpd = make_server("0.0.0.0", port, dispatcher)
    print("serving http on port {0}...".format(str(port)))
    httpd.serve_forever()
