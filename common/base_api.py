#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 16:20
# @Author  : base_api
import json
import requests
from Apitest.common.readExcel import ExcelUtil
from Apitest.common.write import copy_excel, Write_excel
from Apitest.log.logger import logger
def send_requests(s,testdata):
    # mylog = logger().getlog()
    method = testdata["method"]
    url = testdata["url"]
    priority = testdata["priority"]
    print(priority)
    test_nub = testdata["id"]
    try:
        params = eval(testdata["params"])
    except:
        params = None
    try:
        headers = eval(testdata["headers"])
        print("请求头部%s" % headers)
    except:
        headers = None
    type = testdata["type"]
    print("*********正在执行用例*********%s*******************" % test_nub)
    # mylog.info("  ")
    # mylog.info("*********正在执行用例*********%s*******************" % test_nub)
    print("请求方式：%s,请求url：%s" %(method,url))
    print("get请求参数：%s" % params)
    try:
        bodydata = eval(testdata["body"])
    except:
        bodydata = {}
    if type =="data":
        body = bodydata
    elif type == "json":
        body = json.dumps(bodydata)
    else:
        body = bodydata
    if method == "post":print("post请求body类型为：%s，body内容为：%s" % (type,body))
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
        print("接口返回信息：%s" % r.content.decode("utf-8"))
        print("Excel期望值：%s" % testdata['checkpoint'])
        # mylog.info("接口返回信息：%s" % r.content.decode("utf-8"))
        # mylog.info("Excel期望值：%s" % testdata['checkpoint'])
        res["id"] = testdata['id']
        res['rowNum'] = testdata['rowNum']
        res['statuscode'] = str(r.status_code)
        res['text'] = r.content.decode("utf-8")
        res["times"] = str(r.elapsed.total_seconds())
        if res['statuscode']!= "200":
            res["error"] = res['text']
        else:
            res["error"] = ""
        res["msg"] = ""
        if testdata["checkpoint"] in res["text"]:
            res["result"] = "pass"
            print("测试结果为：%s---->%s" % (test_nub,res["result"]))
            # mylog.info("测试结果为：%s---->%s" % (test_nub,res["result"]))
        else:
            res["result"] = "fail"
            print("测试结果为：%s---->%s" % (test_nub, res["result"]))
            # mylog.info("测试结果为：%s---->%s" % (test_nub, res["result"]))
        return res
    except  Exception as msg:
        res["msg"] = str(msg)
        # mylog.log(str(msg))
        return res

def wirte_result(result,filename = r'../data/textcase02.xlsx'):
    row_nub = result['rowNum']
    wt = Write_excel(filename)
    wt.write(row_nub,8,result['statuscode'])
    wt.write(row_nub,12,result['times'])
    wt.write(row_nub,9,result['error'])
    wt.write(row_nub,10,result['result'])
    wt.write(row_nub,12,result['msg'])


if __name__=='__main__':
    data = ExcelUtil('../data/textcase01.xlsx').dict_data()
    for i in data:
        s = requests.session()
        res = send_requests(s,i)
        copy_excel('../data/textcase01.xlsx', '../data/textcase02.xlsx')
        wirte_result(res, filename='../data/textcase02.xlsx')







