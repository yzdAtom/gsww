import scrapy
from ..items import GswwItem

class GswwSpiderSpider(scrapy.Spider):
    name = 'gsww_spider'
    allowed_domains = ['gushiwen.cn']
    # 爬虫开始爬取的网页
    start_urls = ['https://www.gushiwen.cn/default_1.aspx']

    def myprint(self, value):
        print("=" * 30)
        print(value)
        print("=" * 30)

    # response的类型为scrapy.http.response.html.HtmlResponse
    def parse(self, response):
        # print(response.text)
        # self.myprint(type(response))
        # response.xpath返回的都是selector对象
        gsw_divs = response.xpath('//div[@class="left"]/div[@class="sons"]')
        # print(type(gsw_divs))
        for gsw_div in gsw_divs:
            title = gsw_div.xpath('.//b/text()').get()
            # self.myprint(title)
            source = gsw_div.xpath(".//p[@class='source']/a/text()").getall()
            # self.myprint(source)
            if len(source) != 0:
                author = source[0]
                dynasty = source[1]
                # self.myprint({"author":author, "dynasty":dynasty})
                content_list = gsw_div.xpath(".//div[@class='contson']//text()").getall()
                content = "".join(content_list).strip()
                # self.myprint(content)
                item = GswwItem(title=title, dynasty=dynasty, author=author, content=content)
                yield item
            else:
                continue

        next_href = response.xpath('//a[@id="amore"]/@href').get()
        # print(next_href)
        if next_href:
            next_url = response.urljoin(next_href)
            # self.myprint(next_url)
            request = scrapy.Request(next_url)
            yield request