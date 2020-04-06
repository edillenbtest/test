# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class InternshipScrapyPipeline(object):
    # def __init__(self):
    #     self.db = 'internship_scrapy'
    #     self.user = 'root'
    #     self.passwd = 'internship'
    #     self.host = 'localhost'
    
    # def open_spider(self, spider):
    #     self.conn = pymysql.connect(db=self.db,
    #         user=self.user, passwd=self.passwd,
    #         host=self.host,
    #         charset='utf8', use_unicode=True)
    #     self.cursor = self.conn.cursor()
    
    def process_item(self, item, spider):
        # sql = "INSERT INTO table (field1, field2) VALUES (%s, %s)"
        # self.cursor.execute(sql,
        #     (
        #         item.get("field1"),
        #         item.get("field2"),
        #     )
        # )
        # self.conn.commit()
        return item
    
    # def close_spider(self, spider):
    #     self.conn.close()
