# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ClItem(scrapy.Item):
    classfication = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    src = scrapy.Field()
    alt = scrapy.Field()
    ext_name = scrapy.Field()
    domain = scrapy.Field()
    path = scrapy.Field()
    attachment = scrapy.Field()
