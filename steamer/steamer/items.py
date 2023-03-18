# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SteamerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    developer = scrapy.Field()
    reviews = scrapy.Field()
    release_date = scrapy.Field()
    tags = scrapy.Field()
    system_requirements = scrapy.Field()
    customer_reviews = scrapy.Field()
    pass
