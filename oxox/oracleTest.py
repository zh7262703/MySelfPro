import cx_Oracle

connStr = 'newdocncyy/new123456@127.0.0.1/ORCL'


# 查询数据库
def GetDataSet(sql):
    try:
       db = cx_Oracle.connect(connStr)
       # 创建连接
       cr = db.cursor()

       cr.execute(sql)  # 执行sql
       # 返回结果
       rs = cr.fetchall()
       #
       # for x in rs:
       #    print(x)
       cr.close()
       db.close()
       return rs
    except Exception as err:
       return ""


# 操作数据库  1操作成功 0操作失败
def ExecuteSQL(sql):
    try:
        db = cx_Oracle.connect(connStr)
        # 创建连接
        cr = db.cursor()
        cr.execute(sql)  # 执行sql
        cr.close()
        db.commit()
        return 1
    except Exception as err:
        return 0



def PrintRs(rs):
    for x in rs:
        print(x)


#sql = "select * from t_text"
#PrintRs(GetDataSet(sql))


