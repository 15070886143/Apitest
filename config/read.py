#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 10:32
# @Author  : read
from Apitest.config import configread
class readconfig:
    '''创建类，读取配置文件的值'''
    def __init__(self):
        #实例化导入的类
        self.config = configread.ReadConfig()
        #定义一个方法，读取配置文件的值
    def email_read(self):
        mail_host = self.config.get_email('mail_host')
        Smtp_Sender = self.config.get_email('Smtp_Sender')
        Smtp_Password = self.config.get_email('Smtp_Password')
        Smtp_Receivers = self.config.get_email('Smtp_Receivers')
        concont = self.config.get_email('concont')
        #返回值，方便其他模块进行引用
        return mail_host,Smtp_Sender,Smtp_Password,Smtp_Receivers,concont

    def db_read(self):
        usermame = self.config.get_db('username')
        return usermame




