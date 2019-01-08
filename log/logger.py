#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 17:25
# @Author  : logger

'''日志模块'''
import logging
import time
import os

class logger():
    def __init__(self):
        #创建一个logger
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        log_names = '../log/log/'
        # if not os.path.exists(log_names):os.makedirs(log_names)
        #防止请求重复的日志
        if not self.logger.handlers:
            #设置当前时间
            rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            #设置存放日志的名字
            log_name = log_names + rq + '.log'

            ##向文件输出日志
            fh = logging.FileHandler(log_name,encoding='utf-8')
            #设置输出级别
            fh.setLevel(logging.INFO)

            #再设置输入到控制台，即屏幕
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            #定义输入日志的格式
            formafer = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            #设置格式
            fh.setFormatter(formafer)
            ch.setFormatter(formafer)
            # 给logger添加handler
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)
    def getlog(self):
         return self.logger


if __name__=='__main__':
    logger = logger()
    logger.getlog()