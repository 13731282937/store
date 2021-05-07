import random
import pymysql
from util.DBUtils import Update
from util.DBUtils import Select
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
    sql = "select count(*) from jdbcbank"
    data = Select(sql,[])
    if data[0] >= 100:
        return 3

    # 判断是否存在
    sql1 = "select count(*) from jdbcbank where account = %s"
    data2 = Select(sql1,account)
    if data2[0] != 0:
        return 2

    # 正常开户
    # 插入数据
    sql2 = "insert into jdbcbank values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param2 = [account, username, password, counrry, province, street, door, 0, bank_name,]
    # 执行sql
    Update(sql2,param2)
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
        print(info % (account,username,password,counrry,province,street,door,0,bank_name))
    if start == 2:
        print("该用户名已经存在！！！")
    if start == 3:
        print("银行用户库已满！！！")

'''
存钱-----------------------------------------------------------------------------------------------------------
'''
# 存钱逻辑
def bank_addMoney(account,money):
    # 查询表中数据
    sql = "select account from jdbcbank where jdbcbank.account = %s"
    param = [account]
    # 执行sql
    data = Select(sql,param)
    # 获取是否存在输入的account
    num = len(data)

    if num == 1:
        # 修改表中数据
        sql = "update jdbcbank set money = money + %s where account = %s"
        param = [money,account]
        Update(sql,param)
        return 1
    if num == 0:
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
    # 查询表中数据
    sql = "select count(account) from jdbcbank where jdbcbank.account = %s"
    data = Select(sql,account)
    # 获取是否存在输入的account

    if data[0] == 1:
        sql = "select count(*) from jdbcbank where jdbcbank.account = %s and jdbcbank.password = %s"
        param = [account,password]
        data = Select(sql,param)
        if data[0] == 1:
            sql = "select count(*) from jdbcbank where jdbcbank.account = %s and jdbcbank.password = %s and money >= %s"
            param = [account, password,getmoney]
            data = Select(sql,param)
            if data[0] == 1:
                sql = "update jdbcbank set jdbcbank.money =jdbcbank.money - %s where jdbcbank.money >= %s"
                param = [getmoney,getmoney]
                Update(sql,param)
                return 0
            if data[0] == 0:
                return 3
        if [0] == 0:
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
    # 查询表中数据
    sql = "select count(*) from jdbcbank where jdbcbank.account = %s or jdbcbank.account = %s"
    param = [account1,account2]
    # 执行sql
    data = Select(sql,param)

    if data[0] == 2:
        sql = "select count(*) from jdbcbank where jdbcbank.account = %s and jdbcbank.password = %s"
        param = [account1, password]
        data = Select(sql,param)
        if data[0] == 1:
            sql = "select count(*) from jdbcbank where jdbcbank.account = %s and jdbcbank.money >= %s"
            param = [account1,money]
            data = Select(sql,param)
            if data[0] == 1:
                sql = "update jdbcbank set jdbcbank.money = jdbcbank.money - %s where jdbcbank.account = %s"
                param = [money,account1]
                Update(sql,param)
                sql1 = "update jdbcbank set jdbcbank.money = jdbcbank.money + %s where jdbcbank.account = %s"
                param1 = [money,account2]
                Update(sql1, param1)
                return 0
            if data[0] == 0:
                return 3
        if data[0] == 0:
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
    # 查询表中数据
    sql = "select count(*) from jdbcbank where account = %s"
    param = [account]
    # 执行sql
    data = Select(sql,param)
    if data[0] == 1:
        sql = "select count(*) from jdbcbank where account = %s and password = %s"
        param = [account, password]
        data = Select(sql,param)
        if data[0] == 1:
            return 0
        if data[0] == 0:
            return 2
    if data[0] == 0:
        return 1


# 查询方法
def seek():
    account = input("请输入您的要查询的账号：")
    password = input("请输入密码：")
    start = bank_seek(account,password)
    if start == 0:
        # 查询表中数据
        sql = "select * from jdbcbank where account = %s and password = %s"
        param = [account, password]
        # 执行sql
        data = Select(sql, param)
        for i in data:
            username = data[1]
            cunrry = data[3]
            province = data[4]
            street = data[5]
            door = data[6]
            money = data[7]
            bank_name = data[8]
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
        print(info % (account,username,password,cunrry,province,street,door,money,bank_name))
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
