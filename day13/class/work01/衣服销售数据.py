
import xlrd
import xlwt
# 获取工作簿
wb = xlrd.open_workbook(filename="D:\python自动化测试技术\python代码class\python自动化\day13\day13\任务/12月份衣服销售数据.xlsx",encoding_override=True)

# 获取选项卡
sheet = wb.sheet_by_name("12月份各种服饰销售情况")

# 读取行列数据
rows = sheet.nrows
cols = sheet.ncols

num = 0
yrfnum = 0
nzknum = 0
fynum= 0
pcnum = 0
txnum = 0
csnum = 0
day = -1
for i in range(rows):
    data = sheet.row_values(i)
    day = day + 1
    num = num + 1
    for j in data:
        if j == "羽绒服":
            #每日销售量
            data1 = int(data[4])
            #每件价格
            yrfprice = data[2]
            #总销售量
            yrfnum = yrfnum + data1
            #库存
            yrfrepertory = data[3]
        if j == "牛仔裤":
            data1 = int(data[4])
            nzkprice = data[2]
            nzknum = nzknum + data1
            nzkrepertory = data[3]
        if j == "风衣":
            data1 = int(data[4])
            fyprice = data[2]
            fynum = fynum + data1
            fyrepertory = data[3]
        if j == "皮草":
            data1 = int(data[4])
            pcprice = data[2]
            pcnum = pcnum + data1
            pcrepertory = data[3]
        if j == "T血":
            data1 = int(data[4])
            txprice = data[2]
            txnum = txnum + data1
            txrepertory = data[3]
        if j == "衬衫":
            data1 = int(data[4])
            cxprice = data[2]
            csnum = csnum + data1
            csrepertory = data[3]

# 总销售额
grosssales = yrfnum * yrfprice + nzknum * nzkprice + fynum * fyprice + pcnum * pcprice + txnum * txprice + csnum * cxprice
grosssales = round(grosssales,1)

# 平均日销售量
avgdaysell = (yrfnum + nzknum + fynum + pcnum + txnum + csnum)/day
avgdaysell = round(avgdaysell,0)

# 羽绒服本月销售占比
yrfsellthan = yrfnum/yrfrepertory
yrfsellthan = "%.1f%%" % (yrfsellthan * 100)

# 牛仔裤本月销售占比
nzksellthan = nzknum/nzkrepertory
nzksellthan = "%.1f%%" % (nzksellthan * 100)

# 风衣本月销售占比
fysellthan = fynum/fyrepertory
fysellthan = "%.1f%%" % (fysellthan * 100)

# 皮草本月销售占比
pcsellthan = pcnum/pcrepertory
pcsellthan = "%.1f%%" % (pcsellthan * 100)

# T血本月销售占比
txsellthan = txnum/txrepertory
txsellthan = "%.1f%%" % (txsellthan * 100)

# 衬衫本月销售占比
cssellthan = csnum/csrepertory
cssellthan = "%.1f%%" % (cssellthan * 100)

# 创建工作表对象
workbook = xlwt.Workbook(encoding="utf-8")
# 设置表名
sheet1 = workbook.add_sheet('12月份各种服饰销售情况')
sheet2 = workbook.add_sheet('羽绒服')
sheet3 = workbook.add_sheet('牛仔裤')
sheet4 = workbook.add_sheet('风衣')
sheet5 = workbook.add_sheet('皮草')
sheet6 = workbook.add_sheet('T血')
sheet7 = workbook.add_sheet('衬衫')

for i in range(rows):
    for j in range(cols):
        onedata = sheet.cell_value(i, j)
        sheet1.write(i,j,onedata)

sheet1.write(num+2,0,"总销售额:"+str(grosssales))
sheet1.write(num+2,3,"平均日销售量:"+str(avgdaysell))
sheet1.write(num+2,4,"羽绒服本月销售占比:"+str(yrfsellthan))
sheet1.write(num+3,4,"牛仔裤本月销售占比:"+str(nzksellthan))
sheet1.write(num+4,4,"风衣本月销售占比:"+str(fysellthan))
sheet1.write(num+5,4,"皮草本月销售占比:"+str(pcsellthan))
sheet1.write(num+6,4,"T血本月销售占比:"+str(txsellthan))
sheet1.write(num+7,4,"衬衫本月销售占比:"+str(cssellthan))

sheet2.write(0,0,"名称")
sheet2.write(0,1,"本月销售量")
sheet2.write(1,0,"羽绒服")
sheet2.write(1,1,yrfnum)

sheet3.write(0,0,"名称")
sheet3.write(0,1,"本月销售量")
sheet3.write(1,0,"牛仔裤")
sheet3.write(1,1,nzknum)

sheet4.write(0,0,"名称")
sheet4.write(0,1,"本月销售量")
sheet4.write(1,0,"风衣")
sheet4.write(1,1,fynum)

sheet5.write(0,0,"名称")
sheet5.write(0,1,"本月销售量")
sheet5.write(1,0,"皮草")
sheet5.write(1,1,pcnum)

sheet6.write(0,0,"名称")
sheet6.write(0,1,"本月销售量")
sheet6.write(1,0,"T血")
sheet6.write(1,1,txnum)

sheet7.write(0,0,"名称")
sheet7.write(0,1,"本月销售量")
sheet7.write(1,0,"衬衫")
sheet7.write(1,1,csnum)

workbook.save("总数据.xlsx")

