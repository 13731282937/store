

print("请输入身份证号")
idNum=input()
print("请输入姓名")
cname=input()
print("请输入年龄")
age=input()
print("请输入性别")
sex=input()
print("请输入身高")
heig=input()
print("请输入居住地址")
adress=input()

info = '''
    ------------个人信息------------
        身份证号： %s,
        姓名： %s,
        年龄： %s,
        性别： %s,
        身高： %s,
        居住地址： %s
    -------------------------------

'''

print(info % (idNum,cname,age,sex,heig,adress))