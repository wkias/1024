# -*- coding: utf-8 -*-
import scrapy
from ..items import ClItem
from ..settings import META_URL
from ..settings import SELECT
from ..settings import TYPE
from ..settings import DOWNLOAD_HISTORY


class GrassSpider(scrapy.Spider):
    name = 'grass'
    # allowed_domains = []
    start_urls = [META_URL + 'thread.php?fid-' + SELECT + '.html']

    def parse(self, response):
        if response.url.find('thread') == -1:
            item = ClItem()
            item['url'] = response.url
            item['title'] = response.css('h1::text').get()
            item['src'] = response.css('.f14 > img::attr(src)').extract()
            if item['src'].__len__() == 0:
                item['src'] = response.css(
                    '.f14 > a > img::attr(src)').extract()
            if item['src'].__len__() == 0:
                item['src'] = response.css(
                    '.f14 > span > img::attr(src)').extract()
            item['ext_name'] = [i.split('.')[-1] for i in item['src']]
            if any(i.find('/') != -1 for i in item['ext_name']):
                item['alt'] = [str(i+1) + '.' + 'jpg'
                               for i in range(len(item['src']))]
            else:
                item['alt'] = [str(i+1) + '.' + item['ext_name'][i]
                               for i in range(len(item['src']))]
            item['domain'] = META_URL
            item['path'] = response.url.replace(META_URL, '')
            item['classfication'] = TYPE[SELECT]
            # item['attachment'] = response.css('a[href*="download"]::attr(href)').get()
            yield item
        else:
            pages = response.css('.subject::attr(href)').extract()
            if pages.__len__() > 0:
                pages.reverse()
            pages.append(response.css('b+a::attr(href)').get())
            self.log(response.css('.subject::text').extract())
            for i in pages:
                if i not in DOWNLOAD_HISTORY:
                    yield scrapy.Request(META_URL + i, callback=self.parse)
                else:
                    self.log(i + ' has downloaded')
