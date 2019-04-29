import oracleTest

def getMaxId():
   # 数据库查询操作获取最大的id
   sql1 = "select max(id) from T_TEST"
   rs = oracleTest.GetDataSet(sql1)
   oracleTest.PrintRs(rs)
   x = rs[0]
   max_id = 0
   if x[0] == None:
      max_id = 1
   else:
      max_id = int(x[0])+1
   return max_id

#print(x[0])
#print(max_id)

#结束标记
end_flag = 0
T_name = "xxx"
Val1 = "1"
Val2 = "2"
Val3 = "3"
Val4 = "4"


while end_flag == 0:

      if input("请选择操作  A 添加数据 ,B 查询 ：") == "A":
         T_name = input("请输入T_NAME：")
         Val1 = input("请输入Val1：")
         Val2 = input("请输入Val2：")
         Val3 = input("请输入Val3：")
         Val4 = input("请输入Val4：")

         mmid= getMaxId()
         #插入操作
         sql2 = "insert into T_TEST(id,TNAME,VAL1,VAL2,VAL3,VAL4)values("+str(mmid)+",'"+T_name+"','"+Val1+"','"+Val2+"','"+Val3+"','"+Val4+"')"
         resault = oracleTest.ExecuteSQL(sql2)
         if resault > 0:
            print("操作已成功！")
            rs2 = oracleTest.GetDataSet("select * from t_test")
            oracleTest.PrintRs(rs2)
         else:
            print("操作失败！")
      else:
         searchval = input("请输入需要查询的T_NAME:")
         search_sql="select * from t_test where TNAME like '"+searchval+"%'"
         rs2 = oracleTest.GetDataSet(search_sql)
         #print(search_sql)
         if len(rs2) > 0:
            oracleTest.PrintRs(rs2)
         else:
            print("对不起，没有查询到相关的数据！！！")

      if input("是否还要继续数据库操作？Y/N") == "N":
         end_flag = 1



print("欢迎再次使用本系统！")