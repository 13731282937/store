'''
实现输入10个数字，并打印10个数的求和结果

'''

num = 0
sum1 = 0

while num<10:
    num = num +1
    print("请输入数字")
    num1 = input()
    num2 = int(num1)
    sum1 = sum1 + num2

    if num == 10:
        print("输入数字之和为：",sum1)
