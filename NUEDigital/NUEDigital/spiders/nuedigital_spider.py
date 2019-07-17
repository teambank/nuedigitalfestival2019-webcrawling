import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import NueDigitalItem


class NueDigitalSpider(CrawlSpider):
    """
    Class to scrape teambank related content from web pages.
    """
    # define name of crawler
    name = "nuedigital"

    # define start urls
    start_urls = [
            'https://www.easycredit.de/',
            'https://www.teambank.de/',
            'https://www.fymio.de/',
            'https://www.easycredit-ratenkauf.de/',
    ]
    
    # extract domain urls for each start url
    domain_urls = [".".join(domain.split("/")[2].split(".")[-2:]) for domain in start_urls]

    rules = (
        Rule(LinkExtractor(allow_domains=domain_urls, deny="impressum|kontakt"), callback="parse_item", follow=True),
    )

    def parse_item(self, response):
        """
        Method to parse response of http request.

        Returns
        -------
        dict
          Dict with keys "url" and "text".
        """
        # load items dict class
        items = NueDigitalItem()

        # write domain name to items dict
        items["url"] = response.url

        # write text to items dict
        items["text"] = response.body.decode("utf-8")

        yield items