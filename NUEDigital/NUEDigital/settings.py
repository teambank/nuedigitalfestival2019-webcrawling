# -*- coding: utf-8 -*-

# Scrapy settings for NUEDigital project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'NUEDigital'

SPIDER_MODULES = ['NUEDigital.spiders']
NEWSPIDER_MODULE = 'NUEDigital.spiders'

# Enable logging to file
LOG_ENABLED = True
LOG_FILE = "logs.log"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Define maximum depth to crawl any site
DEPTH_LIMIT = 2
# DEPTH_LIMIT = 0 --> no limit

# Adjust the request priority based on its depth
DEPTH_PRIORITY = 2  # positive value for BFO instead of DFO

# export data
FEED_EXPORT_ENCODING = "utf-8"
FEED_FORMAT = "json"
FEED_URI = "items.json"

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

#### Downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # disable default user agent handling
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None, 

    # enabling python package scrapy-user-agents to randomly choose from over 2000 user agents
    # see: https://pypi.org/project/scrapy-user-agents/
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'NUEDigital.pipelines.NuedigitalPipeline': 300,
}

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'NUEDigital.middlewares.NuedigitalSpiderMiddleware': 543,
# }

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'NUEDigital (+http://www.yourdomain.com)'