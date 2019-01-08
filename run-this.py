# coding=utf-8
import unittest
from Apitest.common import HTMLTestRunner_Chart
from Apitest.common import readmail
import os
curpath = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(curpath, "report")
if not os.path.exists(report_path): os.mkdir(report_path)
case_path = os.path.join(curpath, "case")
def add_case(casepath=case_path, rule="test*.py"):
    '''加载所有的测试用例'''
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(casepath,
                                                  pattern=rule,)
    return discover
def run_case(all_case, reportpath=report_path):
    '''执行所有的用例, 并把结果写入测试报告'''
    htmlreport = reportpath+r"\result.html"
    xlsxreport = reportpath+r"\result.xlsx"
    print("测试报告生成地址：%s"% htmlreport)
    fp = open(htmlreport, "wb")
    runner = HTMLTestRunner_Chart.HTMLTestRunner(
        stream=fp,
        title=u'自动化测试报告',
        description='详细测试用例结果',
        # tester=u"杨盼"
    )
    # 调用add_case函数返回值
    runner.run(all_case)
    readmail.sendMail(htmlreport,xlsxreport)
    fp.close()
if __name__ == "__main__":
    cases = add_case()
    run_case(cases)
