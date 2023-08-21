import scrapy
from whisky.items import WhiskyItem


class WhiskySpider(scrapy.Spider):
    name = "whisky"
    start_urls = ["https://www.whiskyshop.com/scotch-whisky/all?item_availability=In+Stock"]

    def parse(self, response):
        for product in response.css("div.product-item-info"):
            try:
                yield {
                    "name": product.css("a.product-item-link::text").get(),
                    "price": product.css("span.price::text").get(),
                    "link":product.css("a.product-item-link").attrib["href"],
                }
            except:
                print(f"product {product} failed" )
                continue
            
            next_page = response.css("a.action.next").attrib["href"]
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)