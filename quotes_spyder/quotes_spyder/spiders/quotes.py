import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    custom_settings = {"FEED_FORMAT": "json", "FEED_URI": "quotes.json"}
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    # def parse(self, response):
    #     for quote in response.xpath("/html//div[@class='quote']"):
    #         yield {
    #             "tags": quote.xpath("div[@class='tags']/a/text()").extract(),
    #             "author": quote.xpath("span/small/text()").get().replace('-', ' '),
    #             "quote": quote.xpath("span[@class='text']/text()").get(),
    #         }
    #     next_link = response.xpath("//li[@class='next']/a/@href").get()
    #     if next_link:
    #         yield scrapy.Request(url=self.start_urls[0] + next_link)

    def parse(self, response):
        for quote in response.css("html div.quote"):
            yield {
                "tags": quote.css("div.tags a::text").extract(),
                "author": quote.css("span small::text").get().replace('-', ' '),
                "quote": quote.css("span.text::text").get(),
            }
        next_link = response.css("li.next a::attr(href)").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)

