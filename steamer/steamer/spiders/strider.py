import scrapy
from pathlib import Path

class SteamSpider(scrapy.Spider):
    name = "strider"
    
    def start_requests(self):
        url = "https://quotes.toscrape.com/js/"
        yield scrapy.Request(url, meta={'playwright': True})
    
    def parse(self, response):
        pass