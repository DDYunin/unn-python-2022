from colorsys import yiq_to_rgb
from subprocess import call
import scrapy

class ArticleSpider(scrapy.Spider):
    name = 'habr'
    start_urls = ['https://habr.com/ru/users/reug/']

    # Первоначальная ссылка, которая ведёт в посты пользователяку
    # response.css('span.tm-tabs__tab-item a::attr(href)')[1].get()

    # Количество постов
    # response.css('span.tm-tabs__tab-counter::text').get().strip()

    # Ссылка на первый пост и соответсвенно и так далее
    # response.css('a.tm-article-snippet__readmore::attr(href)')[0].get()

    # Название статьи
    # response.css('h1.tm-article-snippet__title span::text').get()

    # Необходимая инфа
    # response.css('a.tm-article-snippet__title-link::attr(href)')[0].get()
    # response.css('a.tm-article-snippet__title-link span::text')[0].get()
    # response.css('a.tm-user-card__nickname::text').get().strip().replace('@', '')

    def parse(self, response):
        link_user_posts = response.css('span.tm-tabs__tab-item a::attr(href)')[1].get()
        number_of_posts = response.css('span.tm-tabs__tab-counter::text').get().strip()
        yield response.follow(link_user_posts)
        for number_post in list(range(int(number_of_posts))):
            yield {
                'link':response.css('a.tm-article-snippet__title-link::attr(href)')[number_post].get(),
                'title':response.css('a.tm-article-snippet__title-link span::text')[number_post].get()
            }
