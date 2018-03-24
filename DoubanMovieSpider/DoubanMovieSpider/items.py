# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmoviespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    subject_id = scrapy.Field()
    name = scrapy.Field()
    year = scrapy.Field()
    directors = scrapy.Field()
    actors = scrapy.Field()
    languages = scrapy.Field()
    genres = scrapy.Field()
    runtime = scrapy.Field()
    stars = scrapy.Field()
    channel = scrapy.Field()
    average = scrapy.Field()
    vote = scrapy.Field()
    tags = scrapy.Field()
    watched = scrapy.Field()
    wish = scrapy.Field()
    comment = scrapy.Field()
    question = scrapy.Field()
    review = scrapy.Field()
    discussion = scrapy.Field()
    image = scrapy.Field()
    countries = scrapy.Field()
    summary = scrapy.Field()

