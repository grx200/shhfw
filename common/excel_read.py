import xlrd
###封装了读取excel文件中数据的方法，和ddt结合使用
class ExcelUtil(object):
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # get titles
        self.row = self.table.row_values(0)#取excel标题
        # get rows number
        self.rowNum = self.table.nrows
        # get columns number
        self.colNum = self.table.ncols
        # the current column
        self.curRowNo = 1
    def next(self):
        r = []
        while self.hasNext():
            s = {}
            col = self.table.row_values(self.curRowNo)#取excel数据（标题在第0行，从第1行开始）
            i = self.colNum
            for x in range(i):
                s[self.row[x]] = col[x] #取标题作为键，对应数据作为值，一行数据返回一个字典
            r.append(s) #将一行数据字典添加到一个列表中，列表中的每一个元素代表一行数据，格式为键值对
            self.curRowNo += 1
        return r
    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo:
            return False
        else:
            return True


if __name__ == '__main__':
    excel = ExcelUtil(r'D:\grx_work\software\pycharm\new_shhfw\data\account.xls', 'account')
    data = excel.next()
    print(data)