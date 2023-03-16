#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/22 17:45
# @Author  : configread
import configparser
import os

class ReadConfig:
    """定义一个读取配置文件的类"""
    def __init__(self, filepath=None):#定义起始参数为假
        if filepath:
            #如果没有配置文件，参数=变量
            configpath = filepath
        else:
            #获取当前目录
            root_dir = os.path.dirname(__file__)
            #获取当前目录后，关联后找到文件
            configpath = os.path.join(root_dir, "config.ini")
        self.cf = configparser.ConfigParser()
        #读取文件并设置编码为utf-8
        self.cf.read(configpath,encoding='utf-8')

    def get_email(self,data):#定义一个参数
        return self.cf.get("emali",data)
    def get_db(self,data):
        return self.cf.get("mongdb",data)

