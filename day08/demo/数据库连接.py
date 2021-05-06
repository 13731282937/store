
import pymysql

# 获取数据库连接
con = pymysql.connect(host='localhost',user='root',password='root',database='shopping')

# 创建控制台
cursor = con.cursor()

# 准备一条sql语句
sql = "insert into user values(6,'tom',39,'test6@baomidou.com')"

# 让控制台执行sql
num = cursor.execute(sql)
print("共插入",num,"条")

# 提交数据
con.commit()

# 关闭资源
cursor.close()
con.close()

