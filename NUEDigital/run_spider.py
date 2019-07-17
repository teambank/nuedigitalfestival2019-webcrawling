from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from NUEDigital.spiders.nuedigital_spider import NueDigitalSpider

# define crawling process
process = CrawlerProcess(get_project_settings())

# start crawler
process.crawl(NueDigitalSpider)
process.start()