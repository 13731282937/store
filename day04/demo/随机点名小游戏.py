'''
随机点名小游戏
输入1随机点名
输入2处罚次数
输入q退出系统

技术选型
    random
    if... elif... else
    break
    while
'''


import random

names = ["q","w","e","r","t","y","u"]

while True:
    print("1：随机点名","2：随机处罚")
    print("请输入编号")
    num = input()

    if num.isdigit():
        num = int(num)
        if num == 1:
            num1 = random.randint(0,len(names))
            print("姓名:",names[num1])
        if num == 2:
            cfnum = random.randint(1,101)
            print("处罚次数:",cfnum)
    elif num == "q" or num == "Q":
        print("欢迎下次光临")
        break
    else:
        print("输入非法，请重新输入")