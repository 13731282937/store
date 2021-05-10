'''
分析一个水杯的属性和功能，使用类描述并创建对象
高度，容积，颜色，材质
能存放液体
'''

class water():

    # 高度
    __height = 0
    # 容积
    __volume = 0
    # 颜色
    __color = ""
    #材质
    __texture =""

    def setHeight(self,height):
        self.__height = height
    def getHeight(self):
        return self.__height
    def setVolume(self,volume):
        self.__volume = volume
    def getVolume(self):
        return self.__volume
    def setColor(self, color):
        self.__color  = color
    def getColor(self):
        return self.__color
    def setTexture(self,texture):
        self.__texture = texture
    def getTexture(self):
        return self.__texture

    def store(self):
        print("这个",self.__color,"由",self.__texture,"制作的水杯","能存放",self.__volume,"毫升的液体")


w = water()
w.setHeight("100cm")
w.setColor("绿色")
w.setTexture("玻璃")
w.setVolume(1000)
w.store()