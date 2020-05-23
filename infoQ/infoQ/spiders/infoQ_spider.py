# -*- coding: utf-8 -*-
import scrapy
import json
import requests
from infoQ.items import InfoqItem

class InfoqSpiderSpider(scrapy.Spider):
    name = 'infoQ_spider'
    allowed_domains = ['www.infoq.cn']
    start_urls = ['http://www.infoq.cn/']
    new_url = 'https://www.infoq.cn/public/v1/my/recommond'
    detail_url = 'https://www.infoq.cn/public/v1/article/getDetail'
    score = None

    def parse(self, response):
    	#score = response.meta.get('score','')
    	while True:
    		request = requests.post( self.new_url, 
    			json.dumps({"size":1,"score":self.score}), 
    			headers={'Content-Type':'application/json','Origin':'https://www.infoq.cn'} )
    		dict_str = json.loads(request.text)
    		dic_data = dict_str["data"]
    		self.score = dic_data[-1]['score']
    		print(self.score)
    		for v in dic_data:
    			yield self.article_detail(v["uuid"])
    		if not (dic_data):
    			break



    def article_detail(self,uuid):
    	article_item = InfoqItem()
    	detail_request = requests.post( self.detail_url, 
                   json.dumps({"uuid":uuid}), 
                   headers={'Content-Type':'application/json','Origin':'https://www.infoq.cn'} )
    	article_json = json.loads(detail_request.text)
    	#文章题目
    	article_item['theme'] = article_json['data']['article_title']
    	#文章作者
    	article_item['author'] = ""
    	for v in article_json['data']['author']:
    		article_item['author'] = article_item['author'] + v['nickname'] + ","
    	#文章内容
    	article_item['content'] = article_json['data']['content']
    	#文章发布时间
    	article_item['time'] = article_json['data']['publish_time']
    	#文章标签
    	article_item['topic'] = ""
    	for v in article_json['data']['topic']:
    		article_item['topic'] = article_item['topic'] + v['name'] + ","
    	#文章url
    	article_item['url'] = "https://www.infoq.cn/article/"+uuid
    	#文章介绍
    	article_item['article_summary'] = article_json['data']['article_summary']

    	return article_item
#    	print(article_item)

#    def article_parse(self,response):
#    	article_item = InfoqItem()
 #   	print(response.text)
#    	article_item['theme'] = response.xpath("//div[@class='article-main']/h1/text()").extract()
#    	print(response.xpath("//div[@class='article-main']/h1/text()"))

