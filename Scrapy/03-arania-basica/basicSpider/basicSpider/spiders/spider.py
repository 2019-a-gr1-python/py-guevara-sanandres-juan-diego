import scrapy

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'
    principal_url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
    urls = []
    books_info = {
        'title':[],
        'link':[],
        'price':[]
    }
    flag = True
    def start_requests(self):
        yield scrapy.Request(self.principal_url)
    
    def parse(self, response):
        if(self.flag):
            tag_container = response.css('aside.sidebar.col-sm-4.col-md-3')
            url_gender = tag_container.css('ul.nav.nav-list > li > ul > li > a::attr(href)').extract()
            for url in url_gender:
                self.urls.append(response.urljoin(url))
            self.flag = False
            for url in self.urls:
                yield scrapy.Request(url=url)
        else:
            tag_container = response.css('article.product_pod')
            titles = tag_container.css('h3 > a::text').extract()
            self.fill_titles(titles)
            url_books = tag_container.css('h3 > a::attr(href)').extract()
            self.fill_links(url_books,response)
            prices = tag_container.css('p.price_color::text').extract()
            self.fill_prices(prices)
            self.create_file()
            
    
    def fill_titles(self, titles):
        for title in titles:
            self.books_info['title'].append(title)
    
    def fill_links(self, links, response):
        for url in links:
            self.books_info['link'].append(response.urljoin(url))
    
    def fill_prices(self, prices):
        for price in prices:
            character, value = price.split("£",1)
            self.books_info['price'].append(value)

    def create_file(self):
        f = open("books.txt","w+")
        titles = self.books_info['title']
        links = self.books_info['link']
        prices = self.books_info['price']
        for i in range(titles.__len__()):
            f.write('Book Title: '+titles[i]+'\tLink: '+links[i]+'\tPrice: '+prices[i]+'\t\n')
        f.close()