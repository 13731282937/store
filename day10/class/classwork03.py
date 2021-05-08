'''
编写程序模拟证件上传的功能，让用户输入证件的路径，并拷贝到一个统一的图片路径下。
'''


print("请输入您身份证件的位置:")
add = input()
print("请输入您的身份证号：")
i= input()
address = "D:\python" + "/"+i
f = open(file=add,mode="rb")
f2 = open(file=address,mode="wb")

data = f.readline()
f2.write(data)
f2.close()
f.close()