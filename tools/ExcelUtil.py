import os
import xlrd

class SheetTypeError:
    pass

class ExcelReader:
    def __init__(self,excel_file="testdata.xlsx",sheet_by="美多商城接口测试"):
        """
        #1、验证文件是否存在，存在读取，不存在报错
        :param excel_file: 表格的相对路径
        :param sheet_by: 表格中sheet名称（理解为哪一页）
        :return:
        raise理解
        当程序出错时,python会自动触发异常,也可以通过raise显示引发异常
        一旦执行了raise语句,raise之后的语句不在执行
        如果加入了try,except,那么except里的语句会被执行
                """
        excel_file = "../docs/"+excel_file
        if os.path.exists(excel_file):
            self.excel_file = excel_file
            self.sheet_by = sheet_by
            self._data=list()
        else:
            raise  FileNotFoundError("文件不存在")

    def data(self):
        """
        初始化已经默认传入表格及表格sheet的名称；
        #2、读取sheet方式，名称，索引
        读取sheet内容
        :return:表格结果返回
        """
        if not self._data:                                      #存在不读取，不存在读取
            workbook = xlrd.open_workbook(self.excel_file)
            if type(self.sheet_by) not in [str,int]:
                raise SheetTypeError("请输入Int or Str")
            elif type(self.sheet_by) == int:
                sheet = workbook.sheet_by_index(self.sheet_by)
            elif type(self.sheet_by) == str:
                sheet = workbook.sheet_by_name(self.sheet_by)
            title = sheet.row_values(0)                          #1.获取首行的信息
            for col in range(1,sheet.nrows):                    #2.遍历测试行，与首行组成dict，放在list；#1 循环，过滤首行，从1开始
                col_value = sheet.row_values(col)
                self._data.append(dict(zip(title, col_value)))   #2 与首行组成字典，放list
        return self._data

if __name__ == "__main__":
    print(ExcelReader("安全项目测试进度.xls","邓辉").data())