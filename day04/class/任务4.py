'''
请编程统计列表中的每个数字出现的次数(百度初级测试开发笔试题)
List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
'''

List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
a = len(List) - 1
num = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0

while True:
    num = num + 1
    li = List[a]
    a = a - 1
    if li == 1:
        count1 = count1 + li
    if li == 2:
        count2 = count2 + li
    if li == 3:
        count3 = count3 + li
    if li == 4:
        count4 = count4 + li
    if li == 5:
        count5 = count5 + li
    if li == 6:
        count6 = count6 + li
    if li == 7:
        count7 = count7 + li
    if li == 8:
        count8 = count8 + li
    if li == 9:
        count9 = count9 + li
    if li == 10:
        count10 = count10 + li
    if num == len(List):
        print("1出现次数为：", count1)
        print("2出现次数为：", count2)
        print("3出现次数为：", count3)
        print("4出现次数为：", count4)
        print("5出现次数为：", count5)
        print("6出现次数为：", count6)
        print("7出现次数为：", count7)
        print("8出现次数为：", count8)
        print("9出现次数为：", count9)
        print("10出现次数为：", count10)
        break
