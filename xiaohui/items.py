# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaohuiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class SchoolItem(scrapy.Item):
    table = 'pe_xiaohui'
    image_id = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()