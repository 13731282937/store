'''
编程实现：有names.txt文件，实现用户的注册，登陆，修改密码，上传头像并记录头像路径的功能。（选做）
Names.txt文件内容：
姓名   密码   性别    年龄   地址   头像路径
俞敏洪,admin,男,23,北京市昌平区沙河北大桥桥底下,D:\\picture\\cat.jpg
李彦宏,root,女,27,北京市顺义区金装北大桥桥底下,D:\\picture\\dog.jpg
丁磊,123456,男,53,北京市西城区沙河北大桥桥底下,D:\\picture\\景甜.jpg
麻花藤,admin,男,23,北京市昌平区沙河北大桥桥底下,D:\\picture\\白冰.jpg
码云,admin,男,23,北京市房山区沙河北大桥桥底下,D:\\picture\\杨幂.jpg
邓超,admin,男,23,北京市昌平区沙河北大桥桥底下,D:\\picture\\杨超爷.jpg
'''



def welcome():
    print("----------欢迎进入用户界面--------------")
    print("-   1、注册                          -")
    print("-   2、登录                          -")
    print("-   3、修改密码                       -")
    print("-   4、退出                          -")
    print("-------------------------------------")



# 方法=========================================================================
# 注册
def adduser():
    username = input("请输入您的用户名：")
    password = input("请输入您的密码：")
    sex = input("请输入您的性别：")
    age = input("请输入您的年龄：")
    address = input("请输入你的地址：")
    hendpath = input("请输入您的头像地址：")

    f = open(file="names.txt",mode="a+",encoding="utf-8")
    f.write("\n")
    f.write(username)
    f.write(",")
    f.write(password)
    f.write(",")
    f.write(sex)
    f.write(",")
    f.write(age)
    f.write(",")
    f.write(address)
    f.write(",")
    f.write(hendpath)
    f.write("\n")
    info = '''
        -------账号信息--------
        用户名：%s,
        密码： %s,
        性别： %s,
        年龄： %s,
        地址： %s,
        头像路径： %s
       -----------------------
    '''
    print("注册成功")
    print(info % (username,password,sex,age,address,hendpath))

# 登录
def register():
    username = input("请输入您的用户名:")
    password = input("请输入您的密码:")

    f = open(file="names.txt",mode="r+",encoding="utf-8")
    data = f.readlines()
    a = 0
    for i in data:
        da = i.replace("\n","").split(",")
        if da[0] == username and da[1] == password:
            a = a+1
    if a == 1:
        print("登录成功!")
    if a == 0:
        print("登录失败!")

# 修改密码
def changepassword():
    username = input("请输入您的用户名:")
    password = input("请输入您的密码:")
    password2 = input("请输入您修改后的密码:")

    f = open(file="names.txt", mode="r+", encoding="utf-8")

    data = f.readlines()
    a = 0
    b = 1
    for i in data:
        da = i.replace("\n", "").split(",")
        if da[0] == username and da[1] == password:
            a = a + 1

        b= b+6
    if a == 1:
        print("修改成功")
    if a == 0:
        print("登录失败!")





while True:
    welcome()
    num = input("请输入您要进行的操作编号：")
    if num.isdigit():
        num = int(num)
        if num == 1:
            # 注册
            adduser()
        elif num == 2:
            # 登录
            register()
        elif num == 3:
            # 修改密码
            changepassword()
        elif num == 4:
            # 退出
            print("再见，祝您一路顺风！！！")
            break
        else:
            print("输入非法，请重新输入")
    else:
        print("输入非法，请重新输入")