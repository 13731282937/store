'''
现在有这样一个叫scores.txt的文件，里面有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。但是呢，因为有些魔法作业有一定难度，教授不强制同学们必须上交，所以大家上交作业的次数并不一致。
罗恩 23 35 44
哈利 60 77 68 88 90
赫敏 97 99 89 91 95 90
马尔福 100 85 90

希望你来统计这四个学生的魔法作业的总得分，然后再写入一个txt文件。

'''
num=0
f = open(file="scores.txt",mode="r+",encoding="utf-8")
f2 = open(file="totalscore.txt",mode="w+",encoding="utf-8")
data = f.readlines()
for i in data:
    da = i.replace("\n","").split(" ")
    f2.write(da[0])
    f2.write(" ")
    da1 = da
    del da1[0]
    for i in da1:
        i = int(i)
        num = num +i

    f2.write(str(num))
    f2.write("\n")



f.close()
f2.close()