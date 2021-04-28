'''
编程实现
99乘法表
'''

i = 9

while i >= 1:
    j = 1
    while(j <= i):
        print(i,"*",j,"=", i*j, end='\t')
        j = j + 1
    print('')
    i = i - 1