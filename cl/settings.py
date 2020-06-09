# -*- coding: utf-8 -*-
import os


def get_download_history(DOWNLOAD_HISTORY_STORE):
    if os.path.isfile(DOWNLOAD_HISTORY_STORE):
        with open(DOWNLOAD_HISTORY_STORE, 'r') as f:
            return [i.split(',')[-2].replace('\n', '') for i in f.readlines()]
    else:
        return []


BOT_NAME = 'cl'

# CRITICAL、 ERROR、WARNING、INFO、DEBUG
# LOG_LEVEL = 'DEBUG'
# LOG_FILE = 'scrapy.log'
META_URL = 'https://hjd.wwd5.xyz/2048/'
SELECT = '26'
TYPE = {
    '3': '最新合集',
    '4': '亚洲无码',
    '5': '日本骑兵',
    '13': '欧美新片',
    '15': '国内原创',
    '16': '中字原创',
    '17': '动漫原创',
    '18': '三级写真',
    '19': '转贴交流区',
    '21': '清纯唯美',
    '23': '网友自拍',
    '24': '亚洲激情',
    '25': '欧美激情',
    '26': '露出偷窥',
    '27': '高跟丝袜',
    '28': '卡通动漫',
    '29': 'GIF动图',
    '135': '原创自拍',
    '274': '网络正妹',
    '275': '亚洲正妹',
    '276': '素人正妹',
    '277': 'COSPLAY',
    '278': '女优情报',
}
SPIDER_MODULES = ['cl.spiders']
NEWSPIDER_MODULE = 'cl.spiders'
IMAGES_STORE = './'
DOWNLOAD_HISTORY_STORE = 'scrapy.csv'
PROXY = {
    "http": "http://127.0.0.1:64839",
    "https": "http://127.0.0.1:64839",
}
DEPTH_PRIORITY = 1
# PROXY_ENABLE = True
PROXY_ENABLE = False
DOWNLOAD_HISTORY = get_download_history(DOWNLOAD_HISTORY_STORE)
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.44'

ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 100
# CONCURRENT_REQUESTS_PER_IP = 100

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'USER-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.44'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'scrapy.contrib.spidermiddleware.offsite.OffsiteMiddleware': None,
    # 'cl.middlewares.ClSpiderMiddleware': 100,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'cl.middlewares.ClDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'cl.pipelines.ClPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
