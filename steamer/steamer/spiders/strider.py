import scrapy
from pathlib import Path

class SteamSpider(scrapy.Spider):
    name = "strider"

    def start_requests(self):
        urls = [
            'https://store.steampowered.com/search/?sort_by=Reviews_DESC&supportedlang=english&filter=topsellers&ndl=1'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'steam.html'
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')