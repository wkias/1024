# -*- coding: utf-8 -*-
from .settings import IMAGES_STORE
import os
import requests


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
class SexualPipeline:
    def process_item(self, item, spider):
        fold_name = item['title']
        header = {
            'USER-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        }
        if not os.path.exists(IMAGES_STORE) and len(item['src']) != 0:
            os.mkdir(IMAGES_STORE + fold_name)
        if len(item['src']) == 0:
            with open('../check.txt', 'a+') as fp:
                fp.write(item['title'] + ":" + item['url'])
                fp.write("\n")
        if len(item['alt']) == 0:
            return
        for src, alt in zip(item['src'], item['alt']):
            file_path = IMAGES_STORE + fold_name + '/'
            if not os.path.exists(file_path):
                os.mkdir(file_path)
            with open(file_path + alt + '.jpg', 'wb') as f:
                req = requests.get(src, headers=header)
                f.write(req.content)
        return item
