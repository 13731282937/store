import xlwt
# 创建工作对象
workbook = xlwt.Workbook(encoding=True)

# 设置表名
sheet = workbook.add_sheet("运动商城")

# 录入数据
sheet.write(0,0,"商品")
sheet.write(0,1,"价格")
sheet.write(1,0,"篮球")
sheet.write(1,1,"99")
sheet.write(2,0,"足球")
sheet.write(2,1,"80")
sheet.write(3,0,"乒乓球")
sheet.write(3,1,"3")
sheet.write(4,0,"排球")
sheet.write(4,1,"4")
sheet.write(5,0,"网球")
sheet.write(5,1,"20")
sheet.write(6,0,"运动护膝")
sheet.write(6,1,"200")
sheet.write(7,0,"足球鞋")
sheet.write(7,1,"400")
sheet.write(8,0,"篮球鞋")
sheet.write(8,1,"2000")
sheet.write(9,0,"运动护臂")
sheet.write(9,1,"150")
sheet.write(10,0,"运动手环")
sheet.write(10,1,"100")
sheet.write(11,0,"运动头带")
sheet.write(11,1,"300")
sheet.write(12,0,"特制运动鞋垫")
sheet.write(12,1,"5000")
sheet.write(13,0,"运动袜")
sheet.write(13,1,"180")
sheet.write(14,0,"运动眼镜")
sheet.write(14,1,"3000")
sheet.write(15,0,"运动紧制面具")
sheet.write(15,1,"4000")
sheet.write(16,0,"辣条")
sheet.write(16,1,"600")
sheet.write(17,0,"Lenovo电脑")
sheet.write(17,1,"5000")


# 保持表
workbook.save("D:\python自动化测试技术\python代码class\python自动化\day13\day13\任务\商城.xlsx")