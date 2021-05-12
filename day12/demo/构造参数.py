
class User():
    __username = ""
    __age = 0
    __sex = ""


    def setUsername(self,username):
        self.__username = username

    def getUsername(self):
        return self.__username

    def setAge(self,age):
        self.__age = age

    def getAge(self):
        return self.__age

    def setSex(self,sex):
        self.__sex = sex

    def getSex(self):
        return self.__sex

    def __init__(self,username,age,sex):
        print("1111")
        self.__username = username
        self.__age = age
        self.__sex = sex


u = User("zhangsan",20,"男")

print("我是",u.getUsername(),"我今年",u.getAge(),"岁","我是",u.getSex(),"性")