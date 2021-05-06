import pymysql

con = pymysql.connect(host="localhost",user="root",password="root",database="shopping")

cursor = con.cursor()

sql = "select * from user"

cursor.execute(sql)

data = cursor.fetchall()
print(data)
cursor.close()
con.close()