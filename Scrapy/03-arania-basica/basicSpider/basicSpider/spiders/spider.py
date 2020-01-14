import scrapy

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'
    urls = [
        'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)
    
    def parse(self, response):
        tag_container = response.css('article.product_pod')
        titles = tag_container.css('h3 > a::text').extract()
        url_books = tag_container.css('h3 > a::attr(href)').extract()
        for url in url_books:
            self.urls.append(response.urljoin(url))
        ##url_books_complete = response.urljoin(url_books)
        print(self.urls)
        




