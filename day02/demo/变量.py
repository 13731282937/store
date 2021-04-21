
#1号苹果
id1 = 1
name1 = "苹果"
price1 = 2.3
num1 = 50
qua1 = "A+"
address1 = "平谷"

#2号香蕉
id2 = 2
name2 = "香蕉"
price2 = 3.5
num2 = 100
qua2 = "B+"
address2 = "海南"


print("_________________________________欢迎进入水果商城系统_________________________________")
print("编号\t\t\t名称\t\t\t\t价格\t\t\t\t数量\t\t\t\t品质\t\t\t\t出产地")
print(id1,"\t\t\t",name1,"\t\t\t",price1,"\t\t\t",num1,"\t\t\t",qua1,"\t\t\t",address1,"\t\t\t")
print(id2,"\t\t\t",name2,"\t\t\t",price2,"\t\t\t",num2,"\t\t\t",qua2,"\t\t\t",address2,"\t\t\t")
print("__________________________________________________________________________________")
print("总金额为：￥" , (price1 * num1 +price2 * num2))