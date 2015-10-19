#encoding: utf-8

import scrapy
import re
from scrapy.selector import Selector
from tags.items import QuestionTagsItem
from tags.items import AnswerTagsItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class Question_Tags_Spider(scrapy.Spider):
    name = "question_tags"
    allowed_domains = ['www.healthtap.com']

    f = open('urls_qid.txt')
    start_urls = [ url.strip() for url in f.readlines()  ]
    f.close()
    
    '''
    rules = (
            Rule(LinkExtractor(allow=r"/user_questions/*"),
                callback = "parse_qtags", follow = True),              
            )
    '''

    def parse(self, response):
        item = QuestionTagsItem()
        self.get_qid(response, item)
        self.get_qtags(response, item)
        yield item

    def get_qid(self, response, item):
        qid = response.url.strip().split('/')[-1]
        print "question_id:" + qid
        if qid:
            item['question_id'] = qid

    def get_qtags(self, response, item):
        qtags = response.xpath("//div[@class='also-viewed related-topics'][2]/ul/li/a/text()").extract()
        #print qtopics
        if qtags:
            print qtags
            item['question_tags'] = qtags


#This is for scraping the Answer_tags

class Answer_Tags_Spider(scrapy.Spider):
    name = "answer_tags"
    allowed_domains = ['www.healthtap.com']
    
    f = open('urls_qid.txt')
    start_urls = [ url.strip() for url in f.readlines() ]
    f.close()

    '''
    rules = (
        Rule(LinkExtractor(allow=r"/user_questions/*"),
        callback = "parse_atag", follow = True),
    )
    '''
    def parse(self, response):
        item = AnswerTagsItem()
        for sel in response.xpath("//div[@class='questions-container']/div"):
            self.get_aid(response, sel, item)
            self.get_atags(response, sel, item)
            yield item

    
    def get_aid(self, response, sel, item):
        aid = sel.xpath("@data-answer-id").extract()
        #print "answer_id:" + aid[0]
        if aid:
            print "answer_id:" + aid[0]
            item['answer_id'] = aid[0]

    def get_atags(self, response, sel, item):
        atags = sel.xpath("div[@class='answer clearfix']/div[1]/div[1]//a/text()").extract()
        #print atopics
        if atags:
            print atags
            item['answer_tags'] = atags












