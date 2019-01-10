import scrapy
import csv

class BreadcrumbSpider(scrapy.Spider):
    name = "bread_spider"
    allowed_domains = ['boots.com']
    with open('boots.csv') as file:
        start_urls = [line.strip() for line in file]

        def parse(self, response):
            category = response.css('#widget_breadcrumb li:nth-last-child(1)::text').extract()
            yield{'URL':response,'Category':category}
