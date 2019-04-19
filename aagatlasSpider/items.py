# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AagatlasSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    GeneSymbol = scrapy.Field()
    Disease = scrapy.Field()
    PubMed_ID = scrapy.Field()
    Sentence = scrapy.Field()

class AagatlasGeneSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    GeneSymbol = scrapy.Field()
    Disease = scrapy.Field()
    PubMed_ID = scrapy.Field()
    Sentence = scrapy.Field()