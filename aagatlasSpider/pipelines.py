# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql
from aagatlasSpider.settings import *
import time

class AagatlasspiderPipeline(object):
    def __init__(self):
        """
        初始化
        """
        # 链接数据库
        self.db = pymysql.connect(host=MYSQL_HOST,port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
        # 获取句柄
        self.cursor = self.db.cursor()
        # 获取时间
        self.update_time = time.strftime('%Y-%m-%d',time.localtime())
        # 获取表名
        self.table = MYSQL_TABLE

    def process_item(self, item, spider):
        # print(type(item))
        # print(item['PubMed_ID'])
        # sql = 'select * from aagatlas_disease;'
        # self.cursor.execute(sql)
        # print(self.cursor.fetchone())
        if item['GeneSymbol'] != 'GeneSymbol':
            data = {
                'GeneSymbol':item['GeneSymbol'],
                'Disease':item['Disease'],
                'PubMed_ID':item['PubMed_ID'],
                'Sentence':item['Sentence'],
                'update_time':self.update_time
            }
            # print(data)
            keys = ', '.join(x for x in data.keys())
            # print(keys)
            values = ', '.join(['%s']*len(data))
            # print(values)
            sql = 'insert into {table}({keys}) values({values});'.format(table=self.table, keys=keys, values=values)
            try:
                if self.cursor.execute(sql, tuple(data.values())):
                    self.db.commit()
            except Exception as e:
                self.db.rollback()
                print(e.args)

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()


class AagatlasGeneSpiderPipelines(object):
    def __init__(self):
        """
        初始化
        """
        # 链接数据库
        self.db = pymysql.connect(host=MYSQL_HOST,port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
        # 获取句柄
        self.cursor = self.db.cursor()
        # 获取时间
        self.update_time = time.strftime('%Y-%m-%d',time.localtime())
        # 获取表名
        self.table = MYSQL_TABLE_GENE

    def process_item(self, item, spider):
        # print(type(item))
        # print(item['PubMed_ID'])
        # sql = 'select * from aagatlas_disease;'
        # self.cursor.execute(sql)
        # print(self.cursor.fetchone())
        if item['GeneSymbol'] != 'GeneSymbol':
            data = {
                'GeneSymbol':item['GeneSymbol'],
                'Disease':item['Disease'],
                'PubMed_ID':item['PubMed_ID'],
                'Sentence':item['Sentence'],
                'update_time':self.update_time
            }
            # print(data)
            keys = ', '.join(x for x in data.keys())
            # print(keys)
            values = ', '.join(['%s']*len(data))
            # print(values)
            sql = 'insert into {table}({keys}) values({values});'.format(table=self.table, keys=keys, values=values)
            try:
                if self.cursor.execute(sql, tuple(data.values())):
                    self.db.commit()
            except Exception as e:
                self.db.rollback()
                print(e.args)

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()