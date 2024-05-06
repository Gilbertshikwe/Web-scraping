import scrapy
from scraping.items import MyprojectItem

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://www.remnantrva.com/about']

    def parse(self, response):
        items = MyprojectItem()

        # Extract image URLs
        image_urls = response.css('img::attr(src)').extract()
        
        # Store image URLs in the item
        items['image_urls'] = image_urls

        yield items