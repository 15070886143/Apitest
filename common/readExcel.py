#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 10:17
# @Author  : readExcel
# ##读取表格数据，返回的是一个列表，里面的数据以字典格式存放，通过索引得到字典然后取字典的值

#导入数据驱动模块xlsx
import xlrd
#创建类
class ExcelUtil(object):
    # 此参数为主程序传输过来
    def __init__(self, excelPath):
        # 打开excel文件
        self.data = xlrd.open_workbook(excelPath)
        # 获取excel文档中第一个sheet
        self.table = self.data.sheet_by_index(0)
        print('self.table',self.table)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        print('self.keys',self.keys)
        # 获取总行数
        self.rowNum = self.table.nrows
        print(self.rowNum)
        # 获取总列数
        self.colNum = self.table.ncols
        print(self.colNum)
    def dict_data(self):
        #判断，如果第一个sheet行数小于1行，抛出异常，结束程序
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            #设置空list，用来存储文件中的数据
            r = []
            #设置起始值
            print("r",r)
            #设置遍历的起始行数
            j = 1
            print("j",j)
            #因为第一行是标题所以总行数要-1
            for i in list(range(self.rowNum-1)):
                #创建空对象
                s = {}
                print("self.rowNum-1",self.rowNum-1)
                print("i",i)
                # 从第二行取对应values值
                s['rowNum'] = i+2#当前i=0
                print("s['rowNum']", s['rowNum'])
                #values=第二行的数据，此时j是1
                values = self.table.row_values(j)
                print("values",values)
                #遍历列数，总共13,
                for x in list(range(self.colNum)):
                    print('x',x)
                    #让每一列keys等于values值，这样才不会乱
                    s[self.keys[x]] = values[x]
                    print('s[self.keys[x]]',s[self.keys[x]])
                    print('values[x]',values[x])
                #因为val值赋给了keys，所以把值s拿出来放到新建的list中r
                r.append(s)
                print(r)
                #从一行开始读取数据，最大为rowNum的行数
                j += 1
                print('j',j)
            return r
            print(r)
if __name__ == "__main__":
    excelPath ='../data/textcase01.xlsx'
    data = ExcelUtil(excelPath)
    for i in data.dict_data():
        print(i)
        print(type(i))


# class ExcelUtil():
#      def __init__(self, excelPath, sheetName="Sheet1"):
#          self.data = xlrd.open_workbook(excelPath)
#          self.table = self.data.sheet_by_name(sheetName)
#          # 获取第一行作为key值
#          # 获取总行数
#          self.rowNum = self.table.nrows
#          # 获取总列数
#          self.colNum = self.table.ncols
#      def dict_data(self):
#
#          if self.rowNum > 1:
#              #获取第一列的内容，列表格式
#              keys = self.table.row_values(0)
#              #print(keys)
#              listApiData = []
#              #获取每一行的内容，列表格式
#              for col in range(1,self.rowNum):
#                  values = keys.row_values(col)
#                  # keys，values这两个列表一一对应来组合转换为字典
#                  api_dict = dict(zip(keys, values))
#                  #print(api_dict)
#                  listApiData.append(api_dict)
#
#              return listApiData
#          else:
#              print("表格未填写数据")
#              return None
#
# if __name__ == "__main__":
#     excelPath = r"C:\Users\Administrator\PycharmProjects\untited4\Apitest\data\textcase01.xlsx"
#     sheetName = "Sheet1"
#     data = ExcelUtil(excelPath, sheetName)
#     for i in data.dict_data():
#         print(i)
#         print(type(i))


