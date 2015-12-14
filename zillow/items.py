# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZillowItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    def __setitem__(self, key, value):
        self._values[key] = value
        self.fields[key] = {}

    propertyUrl = scrapy.Field()
    price = scrapy.Field()
    zestimate = scrapy.Field()
    ownerPhone = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    zipcode = scrapy.Field()
    street = scrapy.Field()
    beds = scrapy.Field()
    baths = scrapy.Field()
    sqfts = scrapy.Field()
    priceHistory = scrapy.Field()


