# 人
class People(object):
    __age = None
    __sex = None
    __name = None

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age
    def setSex(self,sex):
        self.__sex = sex
    def getSex(self):
        return self.__sex

# 工人
class Worker(People):

    def work(self):
        print(self.getName() + "正在工作中")

# 学生
class Student(People):
    __numder = ""

    def setNumder(self,numder):
        self.__numder = numder
    def getNumder(self):
        return self.__numder


s = Worker()
s.setName("张三")
s.setSex("男")
s.setAge("18")
s.work()
