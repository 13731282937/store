'''
    商城：
        1.商城
        2.薪资
        3.我的购物车
    逻辑：
        1.初始化您的薪资
        2.展示商城商品
        3.输入商品编号
        4.看钱够不够
            4.1 够了，就添加我的购物车，薪资减去相对应的金额
            4.2 不够，买其他的
        继续卖东西，一直到输入Q或者q，退出
'''
import random
shop = [
    ["篮球",99],
    ["足球",80],
    ["乒乓球",3],
    ["排球",4],
    ["网球",20],
    ["运动护膝",200],
    ["足球鞋",400],
    ["篮球鞋",2000],
    ["运动护臂",150],
    ["运动手环",100],
    ["运动头带",300],
    ["特制运动鞋垫",5000],
    ["运动袜",180],
    ["运动眼镜",3000],
    ["运动紧制面具",4000],
    ["辣条",600],
    ["Lenovo电脑",5000]
]

# 购物车
mycart = []

# 优惠卷
coupon = [
    ["辣条优惠券满600-300",1],
    ["Lenovo电脑半价优惠券",1]
]
# 我的优惠券
coupon1 = []


# 积分
integral = 0

# 2.初始化自己的薪资
salary = input("请输入您的薪资")
salary = input()
#初始总薪资
salary1 = int(salary)
print("薪资为：",salary)


i = random.randint(1,30)
if i >=1 and i <=10:
    coupon1.append(coupon[0])
    print("恭喜您抽中1张辣条优惠券满600-300")
    print("您的优惠券剩余：",coupon1)
if i >= 11 and i<=30:
    coupon1.append(coupon[1])
    print("恭喜您抽中1张Lenovo电脑半价优惠券")
    print("您的优惠券剩余：", coupon1)


while True:
    #3.展示商城商品
    for index,value in enumerate(shop): # enumerate() 枚举：将所有可能都列出来
        print(index,value)

    #输入商品编号：num 是商品编号
    num = input("请输入您要购买的商品编号:")
    num = input()

    # 若是0 1 2 3 4 5 6 7 8 9， 若是 Q或者q：退出 ，若都不是：输入非法
    if num.isdigit(): #检测字符串是否只由数字转成
        num = int(num)
        if num >= len(shop):
            print("商品不存在！！！请您重新输入")
        else:
            #可以买东西
            salary = int(salary)

            if salary >= shop[num][1]:
                if num == 15 and shop[num][1] >=600:
                    if coupon1[0][0] == "辣条优惠券满600-300":
                        print("是否使用优惠券: 0.是  1.不是")
                        change = input()
                        change = int(change)
                        if change == 0:
                            coupon1[0][1] = int(coupon1[0][1])
                            if coupon1[0][1] > 0:
                                mycart.append([shop[num][0],shop[num][1]-300])
                                shop[num][1] = int(shop[num][1])
                                salary = salary - (shop[num][1]-300)
                                coupon1[0][1] = coupon1[0][1]-1
                                print("-------------------------------------")
                                print("添加购物车成功！！！！")
                                print("您的薪资剩余：", salary)
                                print("您的优惠券剩余：", coupon1)
                                print("-------------------------------------")
                            else:
                                print("优惠卷不足")
                        if change == 1:
                            mycart.append(shop[num])
                            shop[num][1] = int(shop[num][1])
                            salary = salary - shop[num][1]
                            print("-------------------------------------")
                            print("添加购物车成功！！！！")
                            print("您的薪资剩余：", salary)
                            print("您的优惠券剩余：", coupon1)
                            print("-------------------------------------")

                elif num == 16:
                    if coupon1[0][0] == "Lenovo电脑半价优惠券":
                        print("是否使用优惠券: 0.是  1.不是")
                        change1 = input()
                        change1 = int(change1)
                        if change1 == 0:
                            coupon1[0][1] = int(coupon1[0][1])
                            if coupon1[0][1] > 0:
                                mycart.append([shop[num][0],shop[num][1]*0.5])
                                shop[num][1] = int(shop[num][1])
                                salary = salary - (shop[num][1]/ 300)
                                coupon1[0][1] = coupon1[0][1] - 1
                                print("-------------------------------------")
                                print("添加购物车成功！！！！")
                                print("您的薪资剩余：", salary)
                                print("您的优惠券剩余：", coupon1)
                                print("-------------------------------------")
                            else:
                                print("优惠券不足")
                        if change1 == 1:

                            mycart.append(shop[num])
                            shop[num][1] = int(shop[num][1])
                            salary = salary - shop[num][1]
                            print("-------------------------------------")
                            print("添加购物车成功！！！！")
                            print("您的薪资剩余：", salary)
                            print("您的优惠券剩余：", coupon1)
                            print("-------------------------------------")

                else:
                #添加购物车
                    mycart.append(shop[num])
                    shop[num][1] = int(shop[num][1])
                    salary = salary - shop[num][1]
                    print("-------------------------------------")
                    print("添加购物车成功！！！！")
                    print("您的薪资剩余：",salary)
                    print("您的优惠券剩余：",coupon1)
                    print("-------------------------------------")
            else:
                print("-------------------------------------")
                print("您的薪资不足，请充值！！！")
                print("-------------------------------------")

    elif num == "q" or num == "Q":

        print("------------您的购物清单为--------------")
        print("-------------------------------------")
        print("购买的商品：")
        for index, value in enumerate(mycart):  # enumerate() 枚举：将所有可能都列出来
            print(index, value)
        print("-------------------------------------")
        print("剩余薪资为：",salary)
        integral = (salary1-salary)/10
        integral = int(integral)
        print("您的积分为：", integral)
        print("您的优惠券剩余：", coupon1)
        print("--------------------------------------")
        print("欢迎您下次光临")
        break
    else:
        print("输入非法，请重新输入")























