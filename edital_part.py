import scrapy

class DnitEditalSpider(scrapy.Spider):
    name = 'dnit_edital'
    start_urls = ['http://www.dnit.gov.br/editais']

    def parse(self, response):
        for edital in response.css('div.edital'):
            yield {
                'nome': edital.css('h3 ::text').get(),
                'link': edital.css('a ::attr(href)').get(),
            }
        next_page = response.css('li.next a ::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

aranha = scrapy.Spider()
dnit = DnitEditalSpider(aranha)
dnit.parse()