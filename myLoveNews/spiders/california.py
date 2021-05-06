import scrapy


class CaliforniaSpider(scrapy.Spider):
    name = 'california'
    allowed_domains = ['seecalifornia.com']
    start_urls = ['http://www.seecalifornia.com/california/california-city-websites.html']

    def parse(self, response):
        print(response)
