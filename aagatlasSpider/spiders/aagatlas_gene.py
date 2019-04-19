# -*- coding: utf-8 -*-

import scrapy
import json
from aagatlasSpider.items import AagatlasGeneSpiderItem

class AagatlasSpider(scrapy.Spider):
    name = 'aagatlas_gene'
    allowed_domains = ['biokb.ncpsb.org']
    start_urls = ['http://biokb.ncpsb.org/aagatlas/index.php/Home/Browse/gene?order=asc&limit=50&offset=0&geneTerm=a']
    part_url = 'http://biokb.ncpsb.org/aagatlas/index.php/Home/Browse/gene?order=asc&geneTerm='
    keywords = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def parse(self, response):
        # 获取响应内容
        content = json.loads(response.text)
        # 获取当前termName的总条数
        total = content['total']
        # 获取termName内容
        rows = content['rows']
        # print('count_row', len(rows))
        # 当前termName
        termName = rows[0]['index']
        # 当前termName的总条目
        page = (int(total)//100 + 1) * 100
        # print(total, page)
        # 真正爬取内容的url
        next_url = self.part_url + termName + '&offset=' + str(page)
        # 爬取所有termName条数
        yield scrapy.Request(next_url, callback=self.parse_index)

        # 爬取其他所有termName
        for kw in self.keywords:
            # 爬取其他所有termName的起始页面
            kw_url = self.part_url + kw + '&limit=50'

            yield scrapy.Request(kw_url, callback=self.parse)

    def parse_index(self, response):
        # 获取响应内容
        content = json.loads(response.text)
        # 获取当前termName的总条数
        total = content['total']
        # print(total)
        # 获取termName内容
        rows = content['rows']
        # print(response.url)
        # print('count_row', total, len(rows))
        for each in rows:
            # http://biokb.ncpsb.org/aagatlas/index.php/Home/Download/gene/genesymbol/BANF1/proteinid/pro~pr:000004637
            # 下载数据的url
            content_url = 'http://biokb.ncpsb.org/aagatlas/index.php/Home/Download/gene/genesymbol/' + each['symbol'] + '/proteinid/' + each['id']
            # print(content_url)
            yield scrapy.Request(content_url, callback=self.parse_content)
            
    def parse_content(self, response):
        
        # print(response.text)
        response_list = response.text.split('\n')
        # print(response_list)
        for each in response_list:

            content_list = each.split(',', 3)
            # print(content_list)
            # print(len(content_list))
            item = AagatlasGeneSpiderItem()
            try:
                item['GeneSymbol'] = content_list[0]
                item['Disease'] = content_list[1]
                item['PubMed_ID'] = content_list[2]
                item['Sentence'] = content_list[3]
            except:
                pass
            # print(item['GeneSymbol'])
            # print(item['Disease'])
            # print(item['PubMed_ID'])
            # print(item['Sentence'])
            if len(item) == 4:
                yield item