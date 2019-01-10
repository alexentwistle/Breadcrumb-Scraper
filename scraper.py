import scrapy
import csv

class BreadcrumbSpider(scrapy.Spider):
    name = "bread_spider"
    allowed_domains = ['lloydspharmacy.com']
    with open('test.csv') as file:
    	start_urls = [line.strip() for line in file]

 
    def parse(self, response):
        category = response.css('#widget_breadcrumb li:nth-last-child(2) ::text').extract_first()
        yield{'URL':response,'Category':category}
