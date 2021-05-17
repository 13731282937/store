'''
    类：就是某一类事务的模板，蓝图
    对象：就是类实体存在。
        封装、继承、多态
        1.封装:
            将所有进行私有化，将属性加上__
            提供set/get方法用于赋值
            1.2 构造方法
                __init__(),用于快速初始化对象
        2.继承：
            狗 -->
            好处：将类与类之间产生一种关系
                提高了父类代码利用率，子类如果父类功能不完善，自己可以完善
            父类：被继承的类叫父类
            子类：继承的类子类
                一个父类可以有多个子类
                多继承：一个子类可以继承多个父类（python是允许，java,c# 不允许有个爹）
                多层继承：父类 --> 子类  -->  孙类
                继承体系：

'''

class Animal:
    name = ""
    age = 0

class Cat(Animal):
    color = ""

    def eat(self,ename):
        print("猫吃",ename)

class Dog(Animal):

    def eat(self,ename):
        print("狗吃",ename)

class Donkey(Animal):

    def eat(self,ename):
        print("驴是",ename)



'''
老手机：
    来电显示：手机号码，来电铃声
新手机：
    来电显示：手机号码，来电铃声，大头贴，来电归属地
'''
import time
class OldPhone(object):
    phoneNumber = ""
    voice = ""

    def call(self,number):
        print(self.phoneNumber,"要打给",number,"，正在响铃",self.voice)
        for i in range(2):
            time.sleep(1)
            print(".",end="")

class NewPhone(OldPhone):
    picture = ""
    add = ""

    def call(self,number):
        # 1. 来电显示继续交给老手机来显示
        super().call(number)

        # 2.新的功能自己来做
        print("我的大头贴是：",self.picture,"来电归属地为：",self.add)

newphone = NewPhone()
newphone.phoneNumber = "13552648187"
newphone.voice = "月亮之上"
newphone.picture = "野猪佩奇"
newphone.add = "美国"
newphone.call("15748569515")
print(NewPhone.__mro__)  # 查看该类的继承路由


# old = OldPhone()
# old.phoneNumber = "13552648187"
# old.voice = "凤凰传奇"
# old.call("15857412521")

class A:
    pass

class B(A):
    pass

class D:
    pass
class C(B,D):
    pass


print(C.__mro__)

















