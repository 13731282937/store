'''
使用while编程实现求1~100以内的数的和！
'''


num = 1
sum1 = 0

while num <= 100:

    sum1 = sum1 + num
    num = num+1

    if num == 100:
        print("1~100以内的数的和！为：",sum1)


