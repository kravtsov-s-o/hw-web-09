import scrapy
from scrapy.crawler import CrawlerProcess
# from spiders.quotes import QuotesSpider
from quotes_spyder.quotes_spyder.spiders.quotes import QuotesSpider
from quotes_spyder.quotes_spyder.spiders.authors import AuthorsSpider

if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(QuotesSpider)
    process.crawl(AuthorsSpider)
    process.start()
