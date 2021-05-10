
# 创建类
class car():

    num  = 0
    color = ""
    peoplenum = 0
    xinghao = ""
    weight = ""

    def run(self):
        print("一辆",self.color,self.xinghao,"拉着",self.peoplenum,"个人在路上跑来跑去")

# 调用类
c = car()

# 给类中对象赋值
c.num = 6
c.color = "红色"
c.peoplenum = 3
c.xinghao = "摇摇车"
c.weight = "500kg"

# 调用类中的方法
c.run()





























