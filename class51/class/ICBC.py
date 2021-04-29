import random

# 银行的数据库，最多储存100个
users = {}

# 银行的名称
bank_name = "中国工商银行的昌平支行"

#

# 打印欢迎界面
def welcome():
    print("----------------------------------------------")
    print("-               JDBC账户管理系统                -")
    print("----------------------------------------------")
    print("- 1.开户                                      -")
    print("- 2.存钱                                      -")
    print("- 3.取钱                                      -")
    print("- 4.转账                                      -")
    print("- 5.查询                                      -")
    print("- 6.退出                                      -")
    print("----------------------------------------------")

'''
# 开户---------------------------------------------------------------------------------------------------------
'''
# 开户逻辑
def bank_addUser(account,username,password,counrry,province,street,door):
    # 判断是否已满
    if len(users) >= 100:
        return 3
    # 判断是否开户
    if account in users:
        return 2
    # 正常开户
    users[account] = {
        "username":username,
        "password": password,
        "counrry": counrry,
        "province": province,
        "street": street,
        "door": door,
        "money": 0,
        "bank_name": bank_name
    }
    return 1

# 开户方法
def addUser():
    # 随机生成账号
    li = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "q", "a", "z", "w", "s", "x", "e", "d", "c", "r", "f", "v",
          "t", "g", "b", "y", "h", "n", "u", "j", "m", "i", "k", "o", "l", "p"]
    account = ''
    for i in range(8):
        index = random.randint(0, len(li) - 1)
        account = account + li[index]
    username = input("请输入您的姓名：")
    password = input("请输入您的密码（6个数字）：")
    print("接下来请输入您的地址信息")
    counrry = input("\t请输入您的国家：")
    province = input("\t请输入省份：")
    street = input("\t请输入街道：")
    door = input("\t请输入门牌号：")
    # 余额不允许第一次输入，需要存钱

    start = bank_addUser(account,username,password,counrry,province,street,door)
    if start == 1:
        print("开户成功!")
        info = '''
            ----------- 个人信息-------------
            账号： %s,
            用户名： %s,
            取款密码： %s,
            地址信息： 
                国家： %s,
                省份： %s,
                街道： %s,
                门牌号： %s,
            余额： %s,
            开户行： %s
            ---------------------------------
        '''
        print(info % (account,username,password,counrry,province,street,door,users[account]["money"],bank_name))
    if start == 2:
        print("该用户名已经存在！！！")
    if start == 3:
        print("银行用户库已满！！！")

'''
存钱-----------------------------------------------------------------------------------------------------------
'''
# 存钱逻辑
def bank_addMoney(account,money):
    if account in users:
        money = int(money)
        users[account]["money"] = users[account]["money"] + money
        return 1
    else:
        return False

#存钱方法
def addMoney():
    account = input("请输入账号：")
    money = input("请输入存储金额：")

    start = bank_addMoney(account,money)
    if start == 1:
        print("存入成功！")
    if start == False:
        print("您输入的账号不存在！")

'''
取钱-----------------------------------------------------------------------------------------------------------
'''
# 取钱逻辑
def bank_withdrawal(account,password,getmoney):
    if account in users:
        if password == users[account]["password"]:
            getmoney = int(getmoney)
            if users[account]["money"] >= getmoney:
                users[account]["money"] = users[account]["money"] - getmoney
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1

# 取钱方法
def withdrawal():
    account = input("请输入账号：")
    password = input("请输入密码：")
    getmoney = input("请输入要取出的金额：")

    start = bank_withdrawal(account,password,getmoney)
    if start == 0:
        print("取款成功！")
    if start == 1:
        print("账号不存在！")
    if start == 2:
        print("密码不对")
    if start == 3:
        print("账户余额不足")

'''
转账-----------------------------------------------------------------------------------------------------------
'''
# 转账逻辑
def bank_transfer(account1,account2,password,money):
    if (account1 in users) and (account2 in users):
        if password == users[account1]["password"]:
            money = int(money)
            if money <= users[account1]["money"]:
                users[account1]["money"] = users[account1]["money"] - money
                users[account2]["money"] = users[account2]["money"] + money
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1

# 转账方法
def transfer():
    account1 = input("请输入您要转出的账号：")
    account2 = input("请输入您要转入的账号：")
    password = input("请输入您转出账号的密码：")
    money = input("请输入您要转出的金额：")

    start = bank_transfer(account1,account2,password,money)
    if start == 0:
        print("转账成功！")
    if start == 1:
        print("您输入的账号不正确！")
    if start == 2:
        print("您输入的密码不正确！")
    if start == 3:
        print("您的账户余额不足！")

'''
查询-----------------------------------------------------------------------------------------------------------
'''
# 查询逻辑
def bank_seek(account,password):
    if account in users:
        if password == users[account]["password"]:
            return 0
        else:
            return 2
    else:
        return 1

# 查询方法
def seek():
    account = input("请输入您的要查询的账号：")
    password = input("请输入密码：")

    start = bank_seek(account,password)
    if start == 0:
        print("以下为您的账号信息")
        info = '''
                ----------- 个人信息-------------
                账号： %s,
                用户名： %s,
                取款密码： %s,
                地址信息： 
                        国家： %s,
                        省份： %s,
                        街道： %s,
                        门牌号： %s,
                余额： %s,
                开户行： %s
                ---------------------------------
                '''
        print(info % (account, users[account]["username"], users[account]["password"], users[account]["counrry"],
                      users[account]["province"], users[account]["street"], users[account]["door"],
                      users[account]["money"], bank_name))
    if start == 1:
        print("该用户不存在")
    if start == 2:
        print("您输入的密码不正确")

while True:
    welcome()
    num = input("请输入您的业务编号：")
    if num.isdigit():
        num = int(num)
        if num == 1:
            # 开户
            addUser()
        elif num == 2:
            # 存款
            addMoney()
        elif num == 3:
            # 取款
            withdrawal()
        elif num == 4:
            # 转账
            transfer()
        elif num == 5:
            # 查询
            seek()
        elif num == 6:
            print("欢迎下次光临！")
            break
        else:
            print("输入非法！！！请重新输入！！！")
    else:
        print("输入非法！！！请重新输入！！！")
