'''

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
    if num1 > num:
        print("大了")
    elif num1 < num:
        print("小了")
    else:
        print("恭喜您猜中了！！！数字为",num,"！！！共猜次数：",count,"次！！！","剩余金额为：",coin)
        break