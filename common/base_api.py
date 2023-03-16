#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 16:20
# @Author  : base_api
import json
import requests
from Apitest.common.readExcel import ExcelUtil
from Apitest.common.write import copy_excel, Write_excel
import xlwt
import xlrd
# from Apitest.log.logger import logger
#传递两参数，主程序传递
def send_requests(s,testdata):
    # mylog = logger().getlog()
    #获取excel文件里的key
    method = testdata["method"]
    url = testdata["url"]
    priority = testdata["priority"]
    test_nub = testdata["id"]
    try:
        params = eval(testdata["params"])
    except:
        params = None
    try:
        headers = eval(testdata["headers"])
        print(f"请求头部{headers}")
    except:
        headers = None
    type = testdata["type"]
    print('\n', f"*********正在执行用例*********{test_nub}*******************", '\n')
    # mylog.info("  ")
    # mylog.info("*********正在执行用例*********%s*******************" % test_nub)
    print(f"请求方式：{method},请求url：{url}")
    print(f"get请求参数：{params}")
    try:
        bodydata = eval(testdata["body"])
    except:
        bodydata = {}
    body = json.dumps(bodydata) if type == "json" else bodydata
    #请求方式，如果为post，输入body内容
    if method == "post":
        print(f"post请求body类型为：{type}，body内容为：{body}")
    verify = False
    res ={}
    try:
        r= s.request(
            method=method,
            url=url,
            params=params,
            headers=headers,
            data=body,
            verify=verify
        )
        # 打印接口返回信息
        print(f'接口返回信息：{r.content.decode("utf-8")}')
        # 打印excel文件的期望值
        print(f"Excel期望值：{testdata['checkpoint']}")
        # mylog.info("接口返回信息：%s" % r.content.decode("utf-8"))
        # mylog.info("Excel期望值：%s" % testdata['checkpoint'])
        #把excel的id添加到res字典
        res["id"] = testdata['id']
        # 获取excel行数
        res['rowNum'] = testdata['rowNum']
        #把接口返回状态码添加到res字典
        res['statuscode'] = str(r.status_code)

        #把接口返回信息添加到字典res
        res['text'] = r.content.decode("utf-8")
        #把接口返回的响应时间添加到字典res
        res["times"] = r.elapsed.total_seconds()
        #如果请求状态码不等于200，就把报错内容写入到error里
        res["error"] = res['text'] if res['statuscode']!= "200" else ""
        res["msg"] = ""
        #如果检查点在接口返回的信息中，则pass，并吧pass添加到excel对应的列中
        res["result"] = "pass" if testdata["checkpoint"] in res["text"] else "fail"
        res["checkuser"] = '杨盼'
        print(f'测试结果为：{test_nub}---->{res["result"]}')
        return res
    except  Exception as msg:
        res["msg"] = str(msg)
        # mylog.log(str(msg))
        return res

def wirte_result(result,filename = r'../case/demotext.xlsx'):
    #获取行数
    row_nub = result['rowNum']
    #调取写入方法
    wt = Write_excel(filename)
    #定义excel样式

    #把值写入到对应列和行数
    wt.write(row_nub,8,result['statuscode'])
    wt.write(row_nub,12,result['times'])
    wt.write(row_nub,9,result['error'])
    wt.write(row_nub,10,result['result'])
    wt.write(row_nub,13,result['msg'])
    wt.write(row_nub,14,result['checkuser'])


if __name__=='__main__':
    #调用读取excel方法
    data = ExcelUtil('../data/textcase01.xlsx').dict_data()
    #遍历excel数据
    for i in data:
        s = requests.session()
        #发送请求
        res = send_requests(s,i)
        #复制文件
        copy_excel('../data/textcase01.xlsx', '../case/demotext.xlsx')
        #传递参数
        wirte_result(res, filename='../case/demotext.xlsx')







