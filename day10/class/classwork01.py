'''
以下文件是用户的一些数据（姓名、年龄、净资产），要求使用数据库工具将文件中的数据写入到数据库中。并统计所有人的资产总和！

'''

import pymysql

# 获取数据库连接
con = pymysql.connect(host="localhost", user="root", password="root", database="day10")
# 创建控制台
cursor = con.cursor()

f = open(file="user.txt",mode="r+",encoding="utf-8")
data = f.readlines()
for i in data:
    da = i.replace("\n","").split(",")
    print(da)
    # 执行的sql语句
    sql = "insert into user(username,age,money) values(%s,%s,%s)"
    param = [da[0],da[1],da[2]]
    cursor.execute(sql,param)
    con.commit()
    f.close()
sql2 = "select sum(money) from user"
cursor.execute(sql2)
sum = cursor.fetchall()
print("所有人的资产总和为：",sum[0])

cursor.close()
con.cursor()

