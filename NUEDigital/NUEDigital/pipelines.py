# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
from bs4 import BeautifulSoup 


class NuedigitalPipeline(object):
    """
    Class to define a pipeline how to handle scraped items.

    Parameter
    --------
    item :
      Automatically provided.

    spider :
      Automatically provided.
    """

    def process_item(self, item, spider):
        """
        Method to process item after scraping and before storing.
        Parses html text and extracts pure text out of html.

        Returns
        -------
        dict
          Dict with keys "url" and "text".
        """
        # parse html 
        soup = BeautifulSoup(item["text"], "html.parser") 

        # exclude java script from html
        for script in soup(["script", "style"]):
            script.decompose()

        # extract pure text
        item["text"] = soup.get_text()

        # remove new lines, tables, multiple whitespace
        item["text"] = re.sub("[\n\t\r ]+", " ", item["text"])

        return item