# -*- coding:utf-8 -*-
from datetime import datetime
from elasticsearch_dsl import Document, Date, Integer, Keyword, Text, connections

# 新建连接
connections.create_connection(hosts=['localhost'])

class myArticleType(Document):
    # 文章类型
    theme = Text(analyzer="ik_max_word")
    url = Keyword()
    author = Keyword()
    content = Text(analyzer="ik_max_word")
    time = Keyword()
    summary = Text(analyzer="ik_max_word")
    topic = Text(analyzer="ik_max_word")

    class Index:
        name = 'infoq'

if __name__ == "__main__":
    myArticleType.init()