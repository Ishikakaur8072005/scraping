import scrapy

class ChocolateSpider(scrapy.Spider):
    # This is the name we use to run the spider in the terminal
    name = 'chocolate_spider'
    
    # The URL of the real business we are scraping
    start_urls = ['https://www.chocolate.co.uk/collections/all']

    def parse(self, response):
        # We find all the 'product-item' containers on the page
        products = response.css('product-item')

        for product in products:
            # We yield a dictionary of the data we want
            yield {
                'name': product.css('a.product-item-meta__title::text').get(),
                # This version looks for the 'money' class which is standard in Shopify stores
                'price': product.css('span.price::text').getall()[-1].strip() if product.css('span.price::text').get() else "N/A",
                'link': response.urljoin(product.css('a.product-item-meta__title::attr(href)').get())
                }

        # Pagination Logic: Find the 'Next' button and follow it
        next_page = response.css('a[rel="next"]::attr(href)').get()
        if next_page:
            # This tells Scrapy to go to the next page and run this 'parse' function again
            yield response.follow(next_page, callback=self.parse)