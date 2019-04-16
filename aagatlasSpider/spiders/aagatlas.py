# -*- coding: utf-8 -*-
import scrapy


class AagatlasSpider(scrapy.Spider):
    name = 'aagatlas'
    allowed_domains = ['biokb.ncpsb.org']
    start_urls = ['http://biokb.ncpsb.org/']

    def parse(self, response):
        print('sdg')
