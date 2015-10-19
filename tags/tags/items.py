# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuestionTagsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    question_id = scrapy.Field()
    question_tags = scrapy.Field()
    #pass


class AnswerTagsItem(scrapy.Item):
    answer_id = scrapy.Field()
    answer_tags = scrapy.Field()


