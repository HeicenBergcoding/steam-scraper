import scrapy
from scrapy.spiders import CrawlSpider, Rule
from steamer.items import getSteamerLinkItems,SteamerItem
from scrapy.linkextractors import LinkExtractor


class SteamSpider(scrapy.Spider):
    name = "strider"
    rules = (Rule(
 LinkExtractor(
 allow='/app/(.+)/',
 restrict_css='#search_result_container'
 ),
 callback='parse_product'
 ),Rule(LinkExtractor(
 allow='page=(d+)',
 restrict_css='.search_pagination_right')
 ))

    urls = ["https://store.steampowered.com/search/?sort_by=Reviews_DESC&supportedlang=english&filter=globaltopsellers&ndl=1"]

    def parse(self, response):
        gameslinks = response.css('//div[@id="search_resultsRows"]')
        for game in gameslinks:
            game_link = getSteamerLinkItems()
            game_link['link'] = game.css('//').get()
            



