import xlrd

# 获取工作簿
wb = xlrd.open_workbook(filename="D:\python自动化测试技术\classtest\student.xls",encoding_override=True)

# 获取选项卡
sheet = wb.sheet_by_name("基础信息表")

# 获取行列数据
rows = sheet.nrows
cols = sheet.ncols

# 打印数据
# for i in range(rows):
#     for j in range(cols):
#         print(sheet.cell_value(i,j),end="\t")
#     print()

for i in range(cols):
    print(sheet.col_values(i))