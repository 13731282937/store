'''
继续完成上午的猜数字游戏的需求功能。
1.添加计数打印功能
2.添加次数金币功能和7次锁定系统功能【退出】。
'''

import random

num = random.randint(1,101)
count =0
coin = 10000

while True:
    count = count +1
    coin = coin - 5
    print("请输入数字")
    num1 = input()
    num1 = int(num1)
    if count == 7:
        print("猜数失败，游戏已锁定")
        break
    if num1 > num:
        print("大了")
    elif num1 < num:
        print("小了")
    else:
        print("恭喜您猜中了！！！数字为",num,"！！！共猜次数：",count,"次！！！","剩余金额为：",coin)
        break