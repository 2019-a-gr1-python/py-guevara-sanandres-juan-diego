import scrapy

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'
    principal_url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
    def start_requests(self):
        yield scrapy.Request(self.principal_url)
    
    def parse(self, response):
        tag_container = response.css('article.product_pod')
        titles = tag_container.css('h3 > a::text').extract()
        url_books = tag_container.css('a > img::attr(src)').extract()
        prices = tag_container.css('p.price_color::text').extract()
        self.create_file(titles,url_books,prices)
        dep_url = response.css('li.next > a::attr(href)').extract()
        if(dep_url):
            yield scrapy.Request(response.urljoin(dep_url[0]))
             
    def create_file(self,titles,links,prices):
        f = open("books.txt","a")
        for i in range(len(titles)):
            f.write('Book Title: '+titles[i]+'\tLink: '+links[i]+'\tPrice: '+prices[i]+'\t\n')
        f.close()