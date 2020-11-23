#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   redis_demo.py
@Version :   1.0
@Author  :   huangsv  
@Contact :   huangsv@outlook.com
@License :   (C)Copyright 2020-2021, Liugroup-NLPR-CASIA
@Time    :   2020/11/23 下午 07:18
'''
import redis


def create(r):
    r.set('name', 'byte')
    r.set('age', 22)
    r.set('gender', '男')

    # 添加 list
    for i in range(1, 11):
        r.rpush('number', i)


def update(r):
    r.set('name', 'huangsv')
    # 追加
    r.append('name', '@outlook.com')


def delete(r):
    r.delete('name')


def select(r):
    print(r.get('name'))
    k_list = r.keys('*')
    print(k_list)
    context = r.mget('age', 'gender', 'name')
    print(context)
    print(r.lrange('number', 0, -1))


if __name__ == '__main__':
    ip = '127.0.0.1'
    pw = '密码'
    try:
        r = redis.StrictRedis(host=ip, port=6379, password=pw, db=5, decode_responses=True)
    except:
        pass
    else:
        create(r)
        update(r)
        select(r)
        delete(r)
