# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UsersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    user_id = scrapy.Field()
    user_email = scrapy.Field()
    user_name = scrapy.Field() 

    user_specialty = scrapy.Field()
    user_intro = scrapy.Field()
    user_exp = scrapy.Field()
    user_address = scrapy.Field()
    
    user_edu = scrapy.Field()
    user_interest = scrapy.Field()
    user_followed = scrapy.Field()
    
    user_saved = scrapy.Field()
    user_helped = scrapy.Field()
    user_agrees = scrapy.Field()
    user_thanks = scrapy.Field()
    user_recommends = scrapy.Field()
    #user_stars = scrapy.Field()


    #pass
