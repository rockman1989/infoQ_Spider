# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from infoQ_ES_dsl import myArticleType

class InfoqPipeline(object):
    def process_item(self, item, spider):
    	article = myArticleType()
    	article.theme = item['theme']
    	article.url = item['url']
    	article.author = item['author']
    	article.content = item['content']
    	article.time = item['time']
    	article.summary = item['article_summary']
    	article.topic = item['topic']
    	#print(article)
    	print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    	article.save()
    	return item
