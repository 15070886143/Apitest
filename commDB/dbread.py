#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 14:19
# @Author  : dbread

import pymysql
import types
# 打开数据库连接
db = pymysql.connect(
    host = '192.168.1.31',
    user = 'rfml_dar451l',
    db = 'test-2',
    password = 'Tfafa_!0llcXf69A'
)
#获取操作游标对象
cousor = db.cursor()
sql = """INSERT INTO wht_statistics_user_daily
    (userid)VALUES
    ('111802222');
      """
try:
    #执行sql语句
    cousor.execute(sql)
    # 提交到数据库执行
    db.commit()
except EnvironmentError as e:
    #发生错误时回滚
    print(e)
    db.rollback()
db.close()
