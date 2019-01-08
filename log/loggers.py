#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 17:00
# @Author  : loggers
import logging
import time
class logger(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        if not self.logger.handlers:
            rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            log_name = '../data/log' + rq + '.log'

            formafer = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logging.basicConfig(filename=log_name,
                                format=formafer, level=logging.DEBUG,
                                filemode='a',
                                datefmt='%Y-%m-%d%I:%M:%S %p')
            fh = logging.FileHandler(log_name, encoding='utf-8')
            fh.setLevel(logging.INFO)
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            fh.setFormatter(formafer)
            ch.setFormatter(formafer)
            # 给logger添加handler
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)


    def getlog(self):
        return self.logger
