# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from 

class AagatlasSpider(scrapy.Spider):
    name = 'aagatlas'
    allowed_domains = ['biokb.ncpsb.org']
    start_urls = ['http://biokb.ncpsb.org/']

    def parse(self, response):
        print('sdg')
