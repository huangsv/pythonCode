#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   mongodb_demo.py
@Version :   1.0
@Author  :   huangsv  
@Contact :   huangsv@outlook.com
@License :   (C)Copyright 2020-2021, Liugroup-NLPR-CASIA
@Time    :   2020/11/23 下午 07:47
'''
import pymongo

def create(col):
    ict = {"name": "CloudByte", "url": "https://cloudbyte.club", 'alexa': 1}
    ist = [
        {"_id": 1, "name": "CB", "url": "https://cloudbyte.com", 'alexa': 0},
        {"_id": 2, "name": "Google", "url": "https://google.club", 'alexa': 1},
    ]
    col.insert_one(ict)
    col.insert_many(ist)

    # 排序
    # mydoc = col.find().sort("name", -1)  # 降序
    mydoc = col.find().sort("name")
    for x in mydoc:
        print(x)


def update(col):
    # 修改第一条匹配到的记录
    # myquery = {"name": "CB"}
    # newvalues = {"$set": {"name": "CByte"}}
    # col.update_one(myquery, newvalues)

    # 批量修改
    myquery = {"name": {"$regex": "^C"}}
    newvalues = {"$set": {"alexa": 1}}
    x = col.update_many(myquery, newvalues)
    print(x.modified_count, "文档已修改")


def select(col):
    col.find_one()
    # 将要返回的字段对应值设置为 1
    # for x in col.find({}, {'_id': 0, 'name': 1}):
    # for x in col.find({}, {'name': 0}):
    for x in col.find():
        print(x)

    # 按条件
    myquery = {"name": "Google"}
    # myresult = col.find().limit(2)  # 显示现两条
    # myquery = {"name": {"$gt": "H"}}  # 查询 name 第一个字符大于H的
    mydoc = col.find(myquery)
    for x in mydoc:
        print(x)


def delete(col):
    myquery = {"name": "CByte"}
    col.delete_one(myquery)

    # 批量删除多个
    # myquery = {"name": {"$regex": "^C"}}
    # x = col.delete_many(myquery)
    # print(x.deleted_count, "个文档已删除")


if __name__ == '__main__':
    try:
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client['byte']
        collist = db.list_collection_names()
        # collist = db.collection_names()
        if "sites" in collist:  # 判断 sites 集合是否存在
            print("集合存在！")
        else:
            col = db["sites"]
    except:
        pass
    else:
        create(col)
        select(col)
        update(col)
        delete(col)
