# -*- coding: GBK -*-

import json
import urllib
import sys
from resty import PathDispatcher
from wsgiref.simple_server import make_server
import oracleTest

#=urllib.parse.unquote_to_bytes(path).decode('iso-8859-1')

# ���庯���������Ǻ�������������������python������ģ�Ĭ�Ͼ����ˡ�
def application(environ, start_response):
    # �����ļ���������ͺ͵�ǰ����ɹ���code
    start_response('200 OK', [('Content-Type', 'text/html')])
    # environ�ǵ�ǰ������������ݣ�����Header��URL��body������ֻ�漰��get
    # ��ȡ��ǰget������������ݣ�������string����
    params = urllib.parse.parse_qs(environ['QUERY_STRING'])
    # ��ȡget��keyΪname��ֵ
    name = params.get('name', [''])[0]
    no = params.get('no', [''])[0]

    # ���һ�����飬������ֻ��һ���ֵ�
    dic = {'name': name, 'no': no}
    return [json.dumps(dic)]

def hello_world(environ, start_response):
    start_response('200 OK', [('Content-Type','text/html;chartset=utf-8')])
    strval = "hello word ��ھ��Ŀռ�!"    #% (environ['PATH_INFO'].encode('iso-8859-1').decode('utf8')[1:] or 'web')
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
