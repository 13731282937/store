'''
实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
name = "root"
password = "admin"
'''

name = "root"
password = "admin"
num = 0
while num < 3:
    print("请输入用户名")
    name1 = input()
    print("请输入密码")
    password1 = input()
    num = num+1
    if name1 == "root" and password1 == "admin":
        print("登录成功")
        break
    else:
        if num == 3:
            print("该账号已被锁定")
        else:
            print("用户名或密码错误")