'''
声明一个列表，在列表中保存6个学生的信息(6个题1中的字典)
students = [
    {'name':'张三','age':23,'score':88,'tel':'23423532','gender':'男'},
    {'name':'李四','age':26,'score':80,'tel':'12533453','gender':'女'},
    {'name':'王五','age':15,'score':58,'tel':'56453453','gender':'男'},
    {'name':'赵六','age':16,'score':57,'tel':'86786785','gender':'保密'},
    {'name':'小明','age':18,'score':98,'tel':'23434656','gender':'女'},
    {'name':'小红','age':23,'score':72,'tel':'67867868','gender':'女'},
]
1)统计不及格学生的个数
2)统计未成年学生的个数
3)打印手机尾号是8的学生的名字
4)打印最高分和对应的学生的名字
5)将列表按学生成绩从大到小排序
6)删除性别保密的所有学生
'''

students = [
    {'name':'张三','age':23,'score':88,'tel':'23423532','gender':'男'},
    {'name':'李四','age':26,'score':80,'tel':'12533453','gender':'女'},
    {'name':'王五','age':15,'score':58,'tel':'56453453','gender':'男'},
    {'name':'赵六','age':16,'score':57,'tel':'86786785','gender':'保密'},
    {'name':'小明','age':18,'score':98,'tel':'23434656','gender':'女'},
    {'name':'小红','age':23,'score':72,'tel':'67867868','gender':'女'},
]








# 1)统计不及格学生的个数
#不及格人数
fail = 0
for i in students:
    if i['score'] < 60:
        fail = fail + 1
print("不及格学生的个数为：",fail)


# 2)统计未成年学生的个数
#未成年人数
chilpeo = 0
for i in students:
    if i['age'] < 18:
        chilpeo = chilpeo +1
print("未成年学生的个数为：",chilpeo)


# 3)打印手机尾号是8的学生的名字
#尾号为8的学生姓名
name8 = []
for i in students:
    str1 = str(i['tel'])
    strend = str1[-1]
    strend = int(strend)
    if strend / 8 == 1:
        name8.append(i['name'])
print("手机尾号是8的学生的名字为：",name8)


# 4)打印最高分和对应的学生的名字
a = 0
namemax = ''
for i in students:
    score = int(i['score'])
    if score > a:
        a = score
        namemax = i['name']
    if score < a:
        a = a
        namemax = namemax
print("最高分为:",a,"  名字：",namemax)



# 5)将列表按学生成绩从大到小排序
import operator

students2 =sorted(students,key=operator.itemgetter('score'))
print("列表按学生成绩从大到小排序为：",format(students2))

# 6)删除性别保密的所有学生
for i in students:
    if i['age'] == '保密':
        del students[i]
print(students)













