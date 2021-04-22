'''
从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
'''

print("请输入第一个边")
a1=input()

print("请输入第二个边")
b1=input()
print("请输入第三个边")
c1=input()

a=int(a1)
b=int(b1)
c=int(c1)



if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("等边三角形")

    if a!=b and b!=c and c!=a:
        if ((a*a + b*b) == c*c) or ((c*c + b*b) == a*a) or ((a*a + c*c) == b*b):
            print("直角三角形")
        else:
            print("普通三角形")

    if (a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a):
        if ((a*a + b*b) == c*c) or ((c*c + b*b) == a*a) or ((a*a + c*c) == b*b):
            print("直角三角形")
        else:
            print("等腰三角形")
else:
    print("不是三角形")

