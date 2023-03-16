#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/25 14:23
# @Author  : email_module
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from Apitest.config.read import readconfig
from Apitest.log import logger

def sendMail():
    # # 邮件配置
    #实例化类
    config = readconfig()
    #接受类方法的值，并转换为列表形式
    em = list(config.email_read())
    #获取读取后第一个值，依次获取，并定义变量
    mail_host = em[0]
    Smtp_Sender = em[1]
    Smtp_Password = em[2]
    Smtp_Receivers = em[3]
    concont = em[4]
    #创建一个带附件的实例
    msg = MIMEMultipart()
    #定义发件人
    msg['From'] = Smtp_Sender
    #定义收件人
    msg['To'] = Smtp_Receivers
    #定义邮件标题
    msg['Subject'] = concont
    #定义发送后文件的名字和格式
    result_htmlbt = '自动化测试报告.html'
    result_excelbt = '自动化测试报告.xlsx'
    result_html = '../report/result.html'
    result_xslx = r'../report/result.xlsx'
    # #设置html格式参数
    msg.attach ( MIMEText ( concont.encode ( 'utf-8' ) , _subtype = 'html' , _charset = 'utf-8' ) )
    # 构造附件1
    part1 = MIMEBase ( 'application' , 'octet-stream' )#'octet-stream': binary data   创建附件对象
    part1.set_payload ( open ( result_html , 'rb' ).read ())  # 将附件源文件以读取的状态添加到附件对象
    #对附件进行转码
    encoders.encode_base64 ( part1 )
    # 添加头部方法，并解决中文附件名乱码问题
    part1.add_header(
        'Content-Disposition',
        'attachment',
        filename=('gbk', '', f'{result_htmlbt}'),
    )
    #将内容主题添加到msg正文
    msg.attach ( part1 )
    #发送文档附件)
    part2 = MIMEBase ( 'application' , 'octet-stream' )#'octet-stream': binary data   创建附件对象
    part2.set_payload ( open ( result_xslx , 'rb' ).read ( ) )  # 将附件源文件加载到附件对象
    encoders.encode_base64 ( part2 )
    part2.add_header(
        'Content-Disposition',
        'attachment',
        filename=('gbk', '', f'{result_excelbt}'),
    )
    msg.attach ( part2 )
    try:
        #定义smtp邮件格式，传递地址和端口，默认465
        smtpObj = smtplib.SMTP_SSL (mail_host ,465)
        #开始登陆，传递发送账号和密码
        smtpObj.login(Smtp_Sender, Smtp_Password)
        #开始发送，发送者给接受者，把msg内容转换成字符串形式
        smtpObj.sendmail(Smtp_Sender, Smtp_Receivers, msg.as_string())
        print('发送成功')
    except smtplib.SMTPException as e:
        print ('发送失败',e)

if __name__=='__main__':
    sendMail()
