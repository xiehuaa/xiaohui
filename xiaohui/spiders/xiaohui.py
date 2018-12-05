# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from xiaohui.items import SchoolItem
import re

class A51jobSpider(scrapy.Spider):
    name = '51job'
    allowed_domains = ['jianli.51job.com/xiaohui']
    start_urls = ['http://jianli.51job.com/xiaohui/']

    def parse(self, response):
        li_list = response.css('.left .clearfix li')
        for li in li_list:
            item = SchoolItem()
            item['name'] = li.css('a span::text').extract_first()
            url = li.css('a::attr(href)').extract_first()
            pattern = re.compile('https.*?xiaohui/(.*?).html', re.S)
            result = re.match(pattern, url)[1]
            item['url'] = url
            item['image_id'] = result
            yield item

    def start_requests(self):
        base_url = 'http://jianli.51job.com/xiaohui/p'
        for page in range(1, 160):
            url = base_url + str(page)
            yield Request(url, self.parse)

    def get_total_page(self, response):
        li_list = response.css('.left .clearfix li')
        for li in li_list:
            print(li.css('a span::text').extract_first())
            url = li.css('a::attr(href)').extract_first()
            print(url)
            pattern = re.compile('https.*?xiaohui/(.*?).html', re.S)
            result = re.match(pattern, url)
            print(result[1])
