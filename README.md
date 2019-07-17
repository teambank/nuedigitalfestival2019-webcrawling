# NUE Digital Festival 
## DevBBQ@TeamBank on the 15th of July 2019 
## Webscraping, -automation and crawling with Python

____________________________________________________________________

## Presentation (mainly webscraping and -automation)

see PDF for speaker deck <br>
"NUE Digital Festival - Webcrawling slides.pdf" <br> <br>

## Webcrawling

**Necessary** <br>
* **Step 1)** Define desired <a href="https://docs.scrapy.org/en/latest/topics/items.html">output dict</a> in [`items.py`](NUEDigital/NUEDigital/items.py) <br>
* **Step 2)** Define <a href="https://docs.scrapy.org/en/latest/topics/spiders.html#crawlspider">crawler</a> in [`nuedigital_spider.py`](NUEDigital/NUEDigital/spiders/nuedigital_spider.py) <br>
* **Step 3)** <a href="https://docs.scrapy.org/en/latest/topics/practices.html#run-scrapy-from-a-script">Start crawler</a> with [`run_spider.py`](NUEDigital/run_spider.py)


**Optional** 
* <a href="https://docs.scrapy.org/en/latest/topics/settings.html">Configure spider</a> in  [`settings.py`](NUEDigital/NUEDigital/settings.py) (e.g. logging, depth limit, cookies, user agents) <br>
* <a href="https://docs.scrapy.org/en/latest/topics/spider-middleware.html">Customize HTTP Request</a> in [`middleware.py`](NUEDigital/NUEDigital/middlewares.py) (e.g. JavaScript rendering with Selenium)
* <a href="https://docs.scrapy.org/en/latest/topics/item-pipeline.html">Customize HTTP Response</a> processing in [`pipelines.py`](NUEDigital/NUEDigital/pipelines.py) (e.g. Cleaning text, Filtering responses, Write data to database)

see <a href="https://docs.scrapy.org/en/latest/">scrapy docs</a> for detailed description


contact: magdalena.deschner@teambank.de