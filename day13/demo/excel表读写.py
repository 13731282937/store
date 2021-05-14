import xlrd


# 获取工作簿
wb = xlrd.open_workbook(filename="D:\python自动化测试技术\classtest\student.xls",encoding_override=True)

# 通过wb获取选项卡
sheet = wb.sheet_by_name("基础信息表")

# 获取行列数据
rows = sheet.nrows #多少行
cols = sheet.ncols #多少列
#
# for i in range(rows):
#     for j in range(cols):
#         print(sheet.cell_value(i,j),end="\t") #end = ""不换行
#     print()

# 打印每行
for i in range(rows):
    print(sheet.row_values(i))