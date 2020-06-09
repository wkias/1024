# -*- coding: utf-8 -*-
import scrapy
from sexual.items import SexualItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['pmeinv.com', 'mtl.gzhuibei.com']
    # start_urls = ['http://pmeinv.com/']
    # 国产
    # start_urls = ['http://pmeinv.com/pmn/guochanmeinv/_nasisheying__no_107_chenyujie___lanqiushaonv/index.html']
    # 港台
    # start_urls = ['http://pmeinv.com/pmn/gangtaimeinv/_beautyleg__no_1818_anonymity___liantisiwayouhuo/index.html']
    # start_urls = ['http://pmeinv.com/pmn/gangtaimeinv/_taiwannvshen__kakaer___hushi_amp_amp_shengdanfeng_xiezhentupian/index.html']
    # 日韩
    # start_urls = ['http://pmeinv.com/pmn/rihanmeinv/_youwuyouwuguan__vol_163_xinggannvshennovaliyasiwazhuti/index.html']
    start_urls = ['http://pmeinv.com/pmn/rihanmeinv/_minisuka_tv__asami_kondou_jinteng______xingganbaisenei/index.html>']

    def parse(self, response):
        meta_url = 'http://pmeinv.com'
        item = SexualItem()
        item['url'] = response.url
        item['title'] = response.css('body > div.hot-news').xpath('text()').get()
        item['src'] = response.xpath('//img//@src').extract()
        item['alt'] = response.xpath('//img//@alt').extract()
        try:
            item['alt'] = response.xpath('//img//@alt').extract()
        except Exception:
            pass
        yield item
        next_page = response.css('body > div.content > div > ul > a:nth-child(4)').xpath('@href').extract_first()
        if next_page:
            yield scrapy.Request(meta_url + next_page, callback=self.parse)
        else:
            next_sheet = response.css('body > div.sxart > li:nth-child(2) > span > a').xpath('@href').extract_first()
            if next_sheet:
                yield scrapy.Request(meta_url + next_sheet, callback=self.parse)
