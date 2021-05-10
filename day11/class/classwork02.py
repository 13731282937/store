'''
有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）
'''

class computer():
    # 屏幕大小
    __screensize = ""
    # 价格
    __price = 0
    # cpu型号
    __cpumodel = ""
    # 内存大小
    __memorysize = ""
    # 待机时长
    __hour = 0


    def setScreensize(self,screenssize):
        self.__screensize = screenssize
    def getScreensize(self):
        return self.__screensize

    def setPrice(self,price):
        self.__price = price
    def getPrice(self):
        return self.__price

    def setCpumodel(self,cpumodel):
        self.__cpumodel = cpumodel
    def getCpumodel(self):
        return self.__cpumodel

    def setMemorysize(self,menmorysize):
        self.__memorysize = menmorysize
    def getMemorysize(self):
        return self.__memorysize

    def setHour(self,hour):
        self.__hour = hour
    def getHour(self):
        return self.__hour

    def type(self):
        print("这个电脑可以打字",self.__hour,"小时")
    def playgame(self):
        print("这个电脑最多支持玩内存为",self.__memorysize,"的游戏")
    def see(self):
        print("这个电脑可以连续看",self.__hour,"小时视频")


c = computer()
c.setScreensize("16寸")
c.setPrice(10000)
c.setMemorysize("16G")
c.setCpumodel("i7")
c.setHour(10)

c.type()
c.playgame()
c.see()