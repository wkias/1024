# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from ..items import ClItem
from ..settings import META_URL
from ..settings import DOWNLOAD_HISTORY


class GrassSpider(scrapy.Spider):
    name = 'grass'
    # allowed_domains = []
    start_urls = [META_URL + 'thread0806.php?fid=8&type=1']  # 亚洲
    # start_urls = [META_URL + 'thread0806.php?fid=8&type=2']  # 欧美
    # start_urls = [META_URL + 'thread0806.php?fid=8&type=3']  # 动漫
    # start_urls = [META_URL + 'thread0806.php?fid=8&type=4']  # 写真
    # start_urls = [META_URL + 'thread0806.php?fid=8&type=12'] # 其他

    def parse(self, response):
        if response.url.find('htm_data') != -1:
            item = ClItem()
            item['url'] = response.url
            item['title'] = response.css('h4::text').get()
            item['src'] = response.css('img::attr(ess-data)').extract()
            item['ext_name'] = [i.split('.')[-1] for i in item['src']]
            item['alt'] = [str(i+1) + '.' + item['ext_name'][i-1]
                           for i in range(len(item['src']))]
            item['domain'] = META_URL
            item['path'] = response.url.replace(META_URL, '')
            classf = self.start_urls[0].split('=')[-1]
            if classf == '1':
                item['classfication'] = '亚洲'
            elif classf == '2':
                item['classfication'] = '欧美'
            elif classf == '3':
                item['classfication'] = '动漫'
            elif classf == '4':
                item['classfication'] = '写真'
            elif classf == '12':
                item['classfication'] = '其他'
            yield item
        else:
            pages = response.css('h3 a::attr(href)').extract()
            if pages.__len__() > 0:
                pages.reverse()
            pages.append(response.css('.pages a::attr(href)').extract()[-2])
            for i in pages:
                if i not in DOWNLOAD_HISTORY:
                    yield scrapy.Request(META_URL + i, callback=self.parse)
