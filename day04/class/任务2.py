'''
有以下一个列表，求其中是5的倍数的和
a = [1,5,21,30,15,9,30,24]
'''

a = [1,5,21,30,15,9,30,24]
c = len(a)
num = 0
i = 0
sum = 0
while True:
    num = num +1
    if a[i] % 5 == 0:
        sum = sum + a[i]
    i = i + 1
    if num == c:
        print("其中是5的倍数的和是：",sum)
        break