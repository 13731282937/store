
import pymysql
import xlwt
import xlrd
host = "localhost"
user = "root"
password = "root"
databases = "bank"
class DBUtils():


    def Update(self,sql, param):
        # 获取数据库连接
        con = pymysql.connect(host=host, user=user, password=password, database=databases)
        # 创建控制台
        cursor = con.cursor()
        # 执行sql
        cursor.execute(sql, param)
        # 提交
        con.commit()
        # 关闭
        cursor.close()
        con.close()

    def Select(self,sql, param):
        # 获取数据库连接
        con = pymysql.connect(host=host, user=user, password=password, database=databases)
        # 创建控制台
        cursor = con.cursor()
        # 执行sql
        cursor.execute(sql, param)
        # 提交
        con.commit()
        # 获取数据
        return cursor.fetchall()
        # 关闭
        cursor.close()
        con.close()
DB = DBUtils()



class DBorExcel:
    tableName = ""
    excelName = ""

    def Db_to_excel(self,tableName,excelName):
        sql = "select * from "+tableName

        data = DB.Select(sql,[])
        # 创建工作表对象
        workbook = xlwt.Workbook(encoding=True)
        # 设置表名
        sheet = workbook.add_sheet(tableName)
        # 写入数据
        num = 0
        num1 = 0
        # 写入表中
        for i in data:
            num = num +1
            for j in i:
                num1 = num1 + 1
                sheet.write(num-1,num1 - 1,j)
            num1 = 0
        workbook.save(excelName)


    def Excel_to_db(self,excelAdress,excelName,tableName):
        #获取工作簿
        wb = xlrd.open_workbook(filename=excelAdress,encoding_override= True)

        # 通过wb获取选项卡
        sheet = wb.sheet_by_name(excelName)

        # 获取行列数据
        rows = sheet.nrows
        ncols = sheet.ncols
        # 获取每行数据
        for i in range(1,rows):
            data = sheet.row_values(i)
            new_data = ["'{}'".format(i) for i in data]
            sql = "insert into {} values({})".format(tableName,','.join(new_data))
            DB.Update(sql,[])











c= DBorExcel()
a= c.Excel_to_db(excelAdress="D:\python自动化测试技术\python代码class\python自动化\day13\day13\任务/banktest.xlsx",excelName="jdbcbank",tableName="jdbcbank")