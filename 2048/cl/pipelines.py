# -*- coding: utf-8 -*-
import os
import datetime
import requests
from .settings import IMAGES_STORE
from .settings import DOWNLOAD_HISTORY_STORE
from .settings import DEFAULT_REQUEST_HEADERS
from .settings import PROXY
from .settings import PROXY_ENABLE


class ClPipeline:

    def process_item(self, item, spider):
        fold_name = item['title']
        if not os.path.exists(IMAGES_STORE) and len(item['src']) != 0:
            os.mkdir(IMAGES_STORE + fold_name)
        if len(item['alt']) == 0:
            return
        for src, alt in zip(item['src'], item['alt']):
            file_path = IMAGES_STORE + item['classfication']
            if not os.path.exists(file_path):
                os.mkdir(file_path)
            file_path = IMAGES_STORE + item['classfication'] + '/' + fold_name + '/'
            if not os.path.exists(file_path):
                os.mkdir(file_path)
            with open(file_path + alt, 'wb') as f:
                if PROXY_ENABLE:
                    req = requests.get(src, headers=DEFAULT_REQUEST_HEADERS, proxies=PROXY)
                else:
                    req = requests.get(src, headers=DEFAULT_REQUEST_HEADERS)
                f.write(req.content)
        with open(DOWNLOAD_HISTORY_STORE, 'a+') as fp:
            fp.write(datetime.datetime.strftime(datetime.datetime.now(), r'%Y-%m-%d %H:%M:%S ') + ',')
            fp.write(item['classfication'] + ',')
            fp.write(item['title'] + ',')
            fp.write(item['url'] + ',')
            fp.write(item['domain'] + ',')
            fp.write(item['path'] + ',')
            fp.write("\n")
        return item
