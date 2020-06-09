# -*- coding: utf-8 -*-
import os
import datetime
import requests
import uuid
from .settings import IMAGES_STORE
from .settings import DOWNLOAD_HISTORY_STORE
from .settings import DEFAULT_REQUEST_HEADERS
from .settings import PROXY
from .settings import PROXY_ENABLE


class ClPipeline:

    def process_item(self, item, spider):
        # if item['title'] or item['src']:
        #     return
        if not os.path.exists(IMAGES_STORE):
            os.mkdir(IMAGES_STORE)
        file_path = IMAGES_STORE + item['classfication']
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        file_path = IMAGES_STORE + item['classfication'] + '/' + item['title'] + '/'
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        else:
            item['title'] += str(uuid.uuid4())
            file_path = IMAGES_STORE + item['classfication'] + '/' + item['title'] + '/'
            os.mkdir(file_path)
        for src, alt in zip(item['src'], item['alt']):
            with open(file_path + alt, 'wb') as f:
                if PROXY_ENABLE:
                    req = requests.get(src, headers=DEFAULT_REQUEST_HEADERS, proxies=PROXY)
                else:
                    req = requests.get(src, headers=DEFAULT_REQUEST_HEADERS)
                f.write(req.content)
            # if item['attachment'] and item['attachment'].__len__() > 0:
            #     with open(file_path + item['title'], 'wb') as f:
            #         if PROXY_ENABLE:
            #             req = requests.get(src, headers=DEFAULT_REQUEST_HEADERS, proxies=PROXY)
            #         else:
            #             req = requests.get(src, headers=DEFAULT_REQUEST_HEADERS)
            #         f.write(req.content)
        with open(DOWNLOAD_HISTORY_STORE, 'a+') as fp:
            try:
                fp.write(datetime.datetime.strftime(datetime.datetime.now(), r'%Y-%m-%d %H:%M:%S ') + ',')
                fp.write(item['classfication'] + ',')
                fp.write(item['title'] + ',')
                fp.write(item['url'] + ',')
                fp.write(item['domain'] + ',')
                fp.write(item['path'] + ',')
                # fp.write(item['attachemtn'] + ',')
            except Exception:
                pass
            fp.write("\n")
        return item
