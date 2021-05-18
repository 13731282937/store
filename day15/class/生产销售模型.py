'''
开发情景：
面包店：
6个厨师在同时造面包，造完后扔到面包篮子里
5个窗外有5个人，抢买面包

面包篮子只能存300个，
厨师如果发现满了停3秒，然后继续放

跑5分钟时间，统计厨师总共造了多少个，顾客买了多少个。(10/个) 每个顾客付了多少钱。
'''

import threading
import time

num = 0
class Timeend(threading.Thread):
    def run(self) -> None:
        global num
        while True:
            if num < 300:
                time.sleep(1)
                num = num + 1
            if num == 300:
                break
kep = 0
sum1 = 0
class Chef(threading.Thread):
    chefer= ""
    def run(self) -> None:
        cook = 0
        global kep
        global sum1
        while True:
            if kep == 300:
                time.sleep(3)
            if kep < 300:
                cook = cook + 1
                kep = kep + 1
                sum1 = sum1 + 1
                print(self.chefer,"做了一个面包")
            if num == 300:
                print("一共做了",sum1,"个面包")
                break




class Window(threading.Thread):
    name = ""

    def run(self) -> None:
        global kep
        cook1 = 0
        while True:
            if kep >0:
                cook1 = cook1 + 1
                kep = kep - 1
                print(self.name,"买了一个面包")
            if kep <=0:
                print("目前没有面包")
            if num == 300:
                print(self.name,"买了",cook1,"个面包","  花了",cook1*10,"元")
                break

t=Timeend()
t.start()

c = Chef()
c.chefer = "一号"
c.start()
c1 = Chef()
c1.chefer = "二号"
c1.start()
c2 = Chef()
c2.chefer = "三号"
c2.start()
c3 = Chef()
c3.chefer = "四号"
c3.start()
c4 = Chef()
c4.chefer = "五号"
c4.start()
c5 = Chef()
c5.chefer = "六号"
c5.start()

w = Window()
w.name = "张三"
w.start()
w1 = Window()
w1.name = "李四"
w1.start()
w2 = Window()
w2.name = "王五"
w2.start()
w3 = Window()
w3.name = "赵六"
w3.start()
w4 = Window()
w4.name = "铁七"
w4.start()


