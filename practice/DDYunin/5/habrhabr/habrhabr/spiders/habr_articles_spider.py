from subprocess import call
import scrapy

class ArticleSpider(scrapy.Spider):
    name = 'habr'
    start_urls = ['https://habr.com/ru/users/reug/posts']

# Первоначальная ссылка, которая ведёт в посты пользователяку
# response.css('span.tm-tabs__tab-item a::attr(href)')[1].get()

# Количество постов
# response.css('span.tm-tabs__tab-counter::text').get().strip()

# Ссылка на первый пост и соответсвенно и так далее
# response.css('a.tm-article-snippet__readmore::attr(href)')[0].get()

# Название статьи
# response.css('h1.tm-article-snippet__title span::text').get()

    def parse(self, response):
        link_user_posts = response.css('span.tm-tabs__tab-item a::attr(href)')[1].get()
        yield response.follow(link_user_posts)
        for link in response.css('a.tm-article-snippet__readmore::attr(href)'):
            yield response.follow(link, callback=self.parse_post)

    def parse_post(self, response):
        yield {
            'title':str(response.css('h1.tm-article-snippet__title span::text').get())
        }
