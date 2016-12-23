# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class JadwalSolatItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    idKota = Field()
    namaKota = Field()
    hari = Field()
    shubuh = Field()
    terbit = Field()
    dzuhur = Field()
    ashar = Field()
    magrib = Field()
    isya = Field()
