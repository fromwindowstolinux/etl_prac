import scrapy

class StoreSpider(scrapy.Spider):
    name = "store"

    def start_requests(self):
        url = f"https://zuscoffee.com/category/store/melaka"
        yield scrapy.Request(url=url, callback=self.parse)

    # hash for id, dot for class, square bracket for attribute
    def parse(self, response):
        stores = response.css(".elementor-widget-container")
        # print(stores)
        for store in stores:
            store_address = store.css("p::text").get()
            div_eh = store.css("div.extra-hatom")
            for span_et in div_eh:
                store_name = span_et.css("span.entry-title::text").get()
                # print(store_name, store_address)
                yield {
                    'store_name': store_name,
                    'store_address': store_address,
                }
        # print(details)

        next_url = response.css(".page-numbers.next::attr(href)").extract_first()
        
        if next_url:
            yield response.follow(next_url, callback=self.parse)
