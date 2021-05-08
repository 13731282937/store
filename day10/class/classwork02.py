'''
使用python复制一张图片到D盘的python文件夹里。
'''

f = open(file="hub.jpg",mode="rb")
f2 = open(file="D:\python\hub.jpg",mode="wb")
data = f.readline()
f2.write(data)
f2.close()
f.close()
