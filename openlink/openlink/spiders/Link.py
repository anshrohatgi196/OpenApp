import scrapy
from scrapy.http import HtmlResponse
from ..items import MyItem


class ChromeSpider(scrapy.Spider):

    name = "chrome"
    st_no =0
    start_urls = [
        'https://www.google.com/search?q=site:youtube.com+openinapp.co&ei=XiTmY77CBbrh4-EPluCyyA4&start=0'
    ]

    def parse(self, response):
        links = []
        for div in response.css('div.DhN8Cf'):
            link = div.css('a::attr(href)').extract()
            links.append(link)


        item = MyItem()
        item['links'] = links
        yield item

        next_page = 'https://www.google.com/search?q=site:youtube.com+openinapp.co&ei=XiTmY77CBbrh4-EPluCyyA4&start='+str(
            ChromeSpider.st_no)
        if ChromeSpider.st_no <=380:
            ChromeSpider.st_no += 10
            yield response.follow(next_page, callback=self.parse)
