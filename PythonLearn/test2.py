import random
#随机数
secrect=random.randint(1,10)

#自定义函数 用于返回最大值
def getMaxVal(val1,val2):
    if(val1>=val2):
       return val1
    else:
       return val2

print('-------------测试程序---------------')
maxtimes=8
nowtime=0
while nowtime<8:
   temp=input("请输入数字：")
   guess=int(temp)
   if guess==secrect:
      print("大叔大婶大所多")
      print("fsdlfksdklfjsdlkjf")
      haveguess=1
      nowtime=8
   else:
      if guess>secrect:
         print("大了！！");
      else:
         print("小了！！");
   nowtime=nowtime+1
   if nowtime<8:
      print("您还有"+str(maxtimes-nowtime)+"次机会")


print(str(getMaxVal(1,9)))
print("游戏结束！")



