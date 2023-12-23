import scrapy


class AuthorsSpider(scrapy.Spider):
    name = "authors"
    custom_settings = {"FEED_FORMAT": "json", "FEED_URI": "authors.json"}
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        authors = response.css('div.quote span a::attr(href)').extract()

        for author_uri in authors:
            yield scrapy.Request(url=self.start_urls[0] + author_uri,
                                 callback=self.parse_author,
                                 meta={'author_url': author_uri})

        next_link = response.css("li.next a::attr(href)").extract_first()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)

    def parse_author(self, response):
        yield {
            'fullname': response.css('h3.author-title::text').get().replace('-', ' '),
            'born_date': response.css('span.author-born-date::text').get(),
            'born_location': response.css('span.author-born-location::text').get(),
            'description': response.css('div.author-description::text').get(),
        }
