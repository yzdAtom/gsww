import scrapy


class GswwSpiderSpider(scrapy.Spider):
    name = 'gsww_spider'
    allowed_domains = ['gushiwen.cn']
    start_urls = ['http://gushiwen.cn/']

    def parse(self, response):
        pass
