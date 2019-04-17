# -*- coding: utf-8 -*-
import scrapy
import json
from aagatlasSpider.items import AagatlasSpiderItem

class AagatlasSpider(scrapy.Spider):
    name = 'aagatlas'
    allowed_domains = ['biokb.ncpsb.org']
    start_urls = ['http://biokb.ncpsb.org/aagatlas/index.php/Home/Browse/disease?order=asc&offset=50&termName=a']
    part_url = 'http://biokb.ncpsb.org/aagatlas/index.php/Home/Browse/disease?order=asc&termName='
    offset = 0
    keywords = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def parse(self, response):
        # 获取响应内容
        content = json.loads(response.text)
        # 获取内容
        rows = content['rows']
        for each in rows:
            # doid = each['id']
            # print(doid)
            # synonym = each['synonym']
            # print(synonym)
            # http://biokb.ncpsb.org/aagatlas/index.php/Home/Download/disease/term/cerebral%20astrocytoma/id/do~doid:3069
            content_url = 'http://biokb.ncpsb.org/aagatlas/index.php/Home/Download/disease/term/' + each['synonym'] + '/id/' + each['id']

            yield scrapy.Request(content_url, callback=self.parse_content)

        # 判断是否是第一次访问termName，是就访问剩余页数
        if not response.meta.get('page'):
            # 获取当前termName的总条数
            total = content['total']
            # print(total)
            # 当前termName的总页数
            page = int(total)//50 + 1
            # print(page)

            # 当前termName
            termName = rows[0]['index']
            # 爬取剩余的其他页数
            for i in range(1, page):
                # 下一页
                next_url = self.part_url + termName + '&offset=' + str((i+1)*50)
                # print(next_url)

                yield scrapy.Request(next_url, callback=self.parse, meta={'page':page})
            
        # 爬取其他所有termName
        for kw in ['B','C']:
            # 爬取其他所有termName的起始页面
            kw_url = self.part_url + kw + '&offset=50'

            yield scrapy.Request(kw_url, callback=self.parse)

            
    def parse_content(self, response):
        
        # print(response.text)
        response_list = response.text.split('\n')
        # print(response_list)
        for each in response_list:

            content_list = each.split(',', 3)
            # print(content_list)
            # print(len(content_list))
            item = AagatlasSpiderItem()
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

            yield item