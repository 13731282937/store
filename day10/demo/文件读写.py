'''
存储数据：
    1、变量
    2、元组、列表、字典、集合
    3、数据库：mysql （pymysql）
    4、文件读写：.txt ()
        1、打开问价
            模式：
                r、w、b(图片、MP3\MP4),a(附加),+可读可写
        2、写入数据
        3、关闭资源
'''


# 打开：句柄，把柄
f = open(file="故事.txt",mode="r+",encoding="utf-8")

# f.write("<天净沙.秋思>\n")
# f.write("枯藤老树昏鸦,\n")
# f.write("小桥流水人家,\n")
# f.write("古道西风瘦马，\n")
# f.write("断肠人在天涯.\n")
# print(f.read())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())


f.close()