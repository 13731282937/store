'''
一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出
'''

heigh=20
heigh1=0
day = 0

while True:
    day = day+1
    heigh1 = heigh1 + 3-2
    heigh2 =heigh1+3

    if  heigh2 >=heigh:
        print("青蛙第",day,"天能出来")
        break