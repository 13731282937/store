'''
从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
'''

num = 0
sum1 = 0
max1 = 0
while num<10:
    num = num +1
    print("请输入数字")
    num1 = input()
    num2 = int(num1)
    sum1 = sum1 + num2
    if max1 <= num2:
        max1 = num2
    else:
        max1

    if num == 10:
        print("一共输入了",num,"个数字")
        print("最大的数为：",max1)
        print("输入数字之和为：",sum1)
        print("输入数字的平均值为",sum1/num)



