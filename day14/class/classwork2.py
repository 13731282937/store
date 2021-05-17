'''
考查知识点：继承的传递性
按要求定义类
要求：
1、定义厨师类，有姓名和年龄的属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的无参数的蒸饭方法；
2、定义厨师的子类，该类中要求只能写一个无返回值的无参数的炒菜的方法，其他的方法不能写；
3、定义厨师的子类的子类，重写所有父类的方法，每个方法的内容只需打印一句话描述方法的功能即可；(蒸饭，炒菜)
4、定义测试类，创建厨师的子类的子类（厨师的孙子类）对象，使用该对象，对厨师类中的姓名和年龄属性赋值，并获取赋值后的属性值打印到控制台上；
5、使用厨师的孙子类对象调用该对象除了getXxx与setXxx以外的其他方法；
'''

class Chef(object):
    __name = None
    __age = None

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age

    def steamRice(self):
        print("正在蒸饭")

class OneChef(Chef):

    def AFriedDish(self):
        print("正在炒菜")

class TweChef(OneChef):
    def steamRice(self):
        print("蒸饭")

    def AFriedDish(self):
        print("炒菜")

class Test(TweChef):
    c = Chef()
    c.setAge(18)
    c.setName("张三")
    print(c.getName(),c.getAge())

tweChef = TweChef()

tweChef.steamRice()
tweChef.AFriedDish()