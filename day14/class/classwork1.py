'''
1、定义老手机类，有品牌属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的带一个Str类型参数的打电话的方法，内容为：“正在给xxx打电话...”
2、定义新手机类，继承老手机类，重写父类的打电话的方法，内容为2句话：“语音拨号中...”、“正在给xxx打电话...”要求打印“正在给xxx打电话...”这一句调用父类的方法实现，不能在子类的方法中直接打印；提供无返回值的无参数的手机介绍的方法，内容为：“品牌为：xxx的手机很好用...”
3、定义测试类，创建新手机对象，并使用该对象，对父类中的品牌属性赋值；
4、使用新手机对象调用手机介绍的方法；
5、使用新手机对象调用打电话的方法；
'''

class OldPhone(object):
    __brand = None

    def setBrand(self,brand):
        self.__brand = brand
    def getBrand(self):
        return self.__brand

    def call(self,phone):
        print("正在给"+phone+"打电话")

class NewPhone(OldPhone):


    def call(self,phone):
        super().call(phone)
        print("语音拨号中...")

    def explain(self):
        print("品牌为："+self.getBrand()  +"的手机很好用...")

class Test(NewPhone):
    phone = "华为"



t= Test()
t.setBrand(t.phone)
t.call("小米")
t.explain()

