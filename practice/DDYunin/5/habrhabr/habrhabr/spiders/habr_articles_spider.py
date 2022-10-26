import scrapy

class ArticleSpider(scrapy.Spider):
    name = 'habr'
    start_urls = ['https://habr.com/ru/users/reug/posts']

    def parse(self, response):
        for link in response.css('dev.tm-article-body a::attr(href)'):
            print(link)
