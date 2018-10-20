# -*- coding: utf-8 -*-

# Scrapy settings for movie project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'movie'

SPIDER_MODULES = ['movie.spiders']
NEWSPIDER_MODULE = 'movie.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'movie (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'movie.middlewares.MovieSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'movie.middlewares.MovieDownloaderMiddleware': 201,
   'movie.middlewares.UserAgentDownloaderMiddleware': 500,
   # 'movie.middlewares.ProxyDownloaderMiddleware': 200,

}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'movie.pipelines.MoviePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

USER_AGENT = ['Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)']

PROXIES = {
    'http': [],
    'https': []
}

# 去重过滤器类: 用于进行请求的去重的. 把已入队请求都存储在Redis数据库中. 从而能够判断该请求是否已经爬取过了
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 调度器类: 把待爬取请求存储到基于Redis队列中.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 配置调取是否需要持久化.
# 如果配置是True, 当爬取结束时候, 它不会清除Redis中的待爬取的请求和已爬指纹
# 如果配置是False, 当爬取结束时候, 它会清除Redis中的待爬取的请求和已爬指纹
SCHEDULER_PERSIST = True
# SCHEDULER_PERSIST = False

# 配置管道[可选]
# ITEM_PIPELINES = {
#     # 用于把爬取数据存储到Redis数据库中[可选]
#     # 'scrapy_redis.pipelines.RedisPipeline': 400,
# }

# 配置Redis数据库的链接:
# 方式1: 配置IP和端口号
# REDIS_IP = '127.0.0.1'
# REDIS_PORT = 6379

# 方式2: Redis的URL
REDIS_URL = 'redis://127.0.0.1:6379/3'


# 1.修改配置文件settings.py添加

ITEM_PIPELINES = {
   # 'tutorial.pipelines.QQNewsPipeline': 300,
   'movie.pipelines.MovieMongoPipeline':400
}
MONGO_URI = 'mongodb://localhost:27017'
MONGO_DB = "movie"