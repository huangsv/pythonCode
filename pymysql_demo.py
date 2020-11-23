#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   connect_mysql.py
@Version :   1.0
@Author  :   huangsv  
@Contact :   huangsv@outlook.com
@License :   (C)Copyright 2020-2021, Liugroup-NLPR-CASIA
@Time    :   2020/11/23 下午 07:04
'''

import pymysql


def create(cursor):
    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS byte")
    # 使用预处理语句创建表
    sql = '''CREATE TABLE byte (
             FIRST_NAME  CHAR(20) NOT NULL,
             LAST_NAME  CHAR(20),
             AGE INT,  
             SEX CHAR(1),
             INCOME FLOAT )'''
    try:
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        return True
    except:
        # 如果发生错误则回滚
        db.rollback()
        return False


def insert(cursor):
    # SQL 插入语句
    sql = "INSERT INTO byte" \
          "(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) " \
          "VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
          ('Mac', 'Mohan', 20, 'M', 2000)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        return True
    except:
        # 如果发生错误则回滚
        db.rollback()
        return False


def select(cursor):
    # SQL 查询语句
    sql = "SELECT * FROM byte WHERE INCOME > %s" % (1000)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            # 打印结果
            print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
                  (fname, lname, age, sex, income))
    except:
        print("Error: unable to fetch data")


def update(cursor):
    # SQL 更新语句
    sql = "UPDATE byte SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        return True
    except:
        # 发生错误时回滚
        db.rollback()
        return False


def delete(cursor):
    # SQL 删除语句
    sql = "DELETE FROM byte WHERE AGE > %s" % (20)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        db.commit()
        return True
    except:
        # 发生错误时回滚
        db.rollback()
        return False


if __name__ == '__main__':
    ip = '101.132.153.251'
    user = 'byte'
    password = 'Byte.123'
    dbname = 'byte'
    try:
        # 打开数据库连接
        db = pymysql.connect(ip, user, password, dbname, charset='utf8')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute("SELECT VERSION()")
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        print("DB version : %s " % data)
    except:
        print('MySQL DB Connect Error')
    else:
        create(cursor)
        insert(cursor)
        select(cursor)
        update(cursor)
        delete(cursor)
    finally:
        # 关闭数据库连接
        cursor.close()
        db.close()
