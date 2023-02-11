import scrapy


class SpiderWebSpider(scrapy.Spider):
    name = "spider_web"
    allowed_domains = ["google.com"]
    start_urls = ["google.com"]

    def parse(self, response):
        pass
