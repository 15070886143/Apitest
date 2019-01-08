#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/25 14:23
# @Author  : email_module
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
def sendMail(result_html,result_xslx):
    # 邮件配置
    mail_host = 'smtp.qq.com'
    Smtp_Sender = '1311375671@qq.com'
    Smtp_Password = 'njdgpxkklmhihcge'
    Smtp_Receivers = ['1311375671@qq.com']
    concont = '请查收！'
    # 创建一个带附件的实例
    msg = MIMEMultipart()
    msg['From'] = Smtp_Sender
    receiver = ','.join(Smtp_Receivers)
    msg['To'] = receiver
    msg['Subject'] = '自动化测试报告'
    # word_name = r'C:\Users\Administrator\PycharmProjects\untitled2\将来的项目\interfaceTest\report\report.html'
    result_html = result_html
    result_xslx = result_xslx
    result_htmlbt = '自动化测试报告.html'
    result_excelbt = '自动化测试报告.xlsx'
    # 邮件正文
    msg.attach ( MIMEText ( concont.encode ( 'utf-8' ) , _subtype = 'html' , _charset = 'utf-8' ) )
    # 构造附件1
    part1 = MIMEBase ( 'application' , 'octet-stream' )#'octet-stream': binary data   创建附件对象
    part1.set_payload ( open ( result_html , 'rb' ).read ( ) )  # 将附件源文件加载到附件对象
    encoders.encode_base64 ( part1 )
    part1.add_header ( 'Content-Disposition' , 'attachment' , filename = ('gbk' , '' , '%s' % result_htmlbt) )  # 给附件添加头文件
    msg.attach ( part1 )
    #发送文档附件)
    part2 = MIMEBase ( 'application' , 'octet-stream' )#'octet-stream': binary data   创建附件对象
    part2.set_payload ( open ( result_xslx , 'rb' ).read ( ) )  # 将附件源文件加载到附件对象
    encoders.encode_base64 ( part2 )
    part2.add_header ( 'Content-Disposition' , 'attachment' , filename = ('gbk' , '' , '%s' % result_excelbt) )  # 给附件添加头文件
    msg.attach ( part2 )
    try:
        smtpObj = smtplib.SMTP_SSL (mail_host , 465)
        smtpObj.login(Smtp_Sender, Smtp_Password)
        smtpObj.sendmail(Smtp_Sender, receiver, msg.as_string())
        print('发送成功')
    except smtplib.SMTPException as e:
        print ('发送失败',e)

if __name__=='__main__':
    sendMail()
