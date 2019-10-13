# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
import scrapy


class FacebookscraperPipeline(object):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.fb_graph
        self.seen = {}

    def process_item(self, item, spider):
        collection = self.mongo_base[spider.name]
        collection.insert_one(item)

        fbid = item.get('fbid')
        self.seen[fbid] = self.seen.get(fbid, 0) + 1
        if self.seen[fbid] == 2:
            spider.crawler.engine.close_spider(self, reason=f'Path is found. Fbid {fbid} seen twice!')
        return item

