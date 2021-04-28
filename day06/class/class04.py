'''
.用三个列表表示三门学科的选课学生姓名(一个学生可以同时选多门课)
语文 = ['小明','小张','小黄','小杨']
数学 = ['小黄','小李','小王','小杨','小周']
英语 = ['小杨','小张','小吴','小冯','小周']

1)求选课学生总共有多少人
2)求只选了第一个学科的人的数量和对应的名字
3)求只选了一门学科的学生的数量和对应的名字
'''

chine = ['小明','小张','小黄','小杨']
math = ['小黄','小李','小王','小杨','小周']
english = ['小杨','小张','小吴','小冯','小周']

# 1)求选课学生总共有多少人
num = 0
peonum = []
for i in chine:
    if i not in peonum:
        peonum.append(i)
        num = num + 1
for i in math:
    if i not in peonum:
        peonum.append(i)
        num = num + 1
for i in english:
    if i not in peonum:
        peonum.append(i)
        num = num + 1
print("=======================================")
print("选课的学生人数为：",num)


# 2)求只选了第一个学科的人的数量和对应的名字
num2 = 0
chineone = []
for i in chine:
    if (i not in math) and (i not in english):
        num2 = num2 + 1
        chineone.append(i)
print("=======================================")
print("只选了第一个学科的人数为：",num2)
print("姓名为：",chineone)


# 3)求只选了一门学科的学生的数量和对应的名字
num3 = 0
classone = []
for i in chine:
    if (i not in math) and (i not in english):
        num3 = num3 + 1
        classone.append(i)
for i in math:
    if (i not in chine) and (i not in english):
        num3 = num3 + 1
        classone.append(i)
for i in english:
    if (i not in math) and (i not in chine):
        num3 = num3 + 1
        classone.append(i)

print("=======================================")
print("只选了一个学科的人数为：",num3)
print("姓名为：",classone)
