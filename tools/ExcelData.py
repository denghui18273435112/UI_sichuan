import xlrd
from config.path import *

def ExcelData(beginColumn=None):
    """
    读取表格中的用例信息
    :param beginColumn:第一列的名称，支持模糊
    :return: 返回的数据格式字典
    """
    _data=[]
    workbook = xlrd.open_workbook(file_path_01)
    sheets = workbook.sheet_names()
    for i in range(workbook.nsheets):
        sheet = workbook.sheet_by_name(sheets[i])
        title = sheet.row_values(0)
        for col in range(1,sheet.nrows):
            col_value = sheet.row_values(col)
            if beginColumn !=None:
                if beginColumn in sheet.cell(col,0).value:
                    _data.append(dict(zip(title, col_value)))
            else:
                    _data.append(dict(zip(title, col_value)))
    return _data

if __name__ == "__main__":
    print(ExcelData("test_overview_digital"))





