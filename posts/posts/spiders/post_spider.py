#encoding : utf-8

import scrapy
import re
from scrapy.selector import Selector
from posts.items import AnswerItem
from posts.items import QuestionItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.exceptions import CloseSpider


class AnswerSpider(scrapy.Spider):
    name = "answer_posts"
    allowed_domains = ['www.healthtap.com']
    
    f = open('urls_qid.txt')
    #f = file('urls.txt', "r")
    start_urls = [ url.strip() for url in f.readlines() ]
    f.close()

    #item_count = 0
    #close_down = False
    
    '''
    rules = (
        Rule(LinkExtractor(allow=r"/user_questions/*"),
        callback = "parse_answer", follow = False),              
    )    
    '''

    def parse(self, response):
        
        '''
        if self.item_count > 10000:
            self.close_down = True

        if self.close_down:
            raise CloseSpider(reason = 'Data Filled')
        '''
        item = AnswerItem()
        for sel in response.xpath("//div[@class='questions-container']/div"):
            self.get_aid(response, sel, item)
            self.get_rid(response, item)
            self.get_uid(response, sel, item)
            self.get_vote(response, sel, item)
            self.get_acontent(response, sel, item)
            #self.item_count = self.item_count + 1

            yield item
    
    def get_aid(self, response, sel, item): 
        aid = sel.xpath("@data-answer-id").extract()
        print "answer_id:" + aid[0]
        if aid:
            item['answer_id'] = aid[0]
        
    def get_rid(self, response, item):
        rid = response.url.strip().split('/')[-1]
        if rid:
            print "related_id:" + rid
            item['related_id'] = rid
    
    def get_uid(self, response, sel, item):
        uid = sel.xpath("div[1]/a/@href").extract()
        print "user_id :" + uid[0].strip().split('/')[-1]
        if uid:
            item['user_id'] = uid[0].strip().split('/')[-1]

    
    def get_vote(self, response, sel, item):
        vote = sel.xpath("div[@class='agrees']/div/span/text()").extract()
        if vote:
            print "answer_vote:" + vote[0]
            item['answer_voted'] = vote[0].strip()
        else :
            item['answer_voted'] = "0"




    def get_acontent(self, response, sel, item):
        answer = sel.xpath("div[@class='answer clearfix']/div[1]/div[1]//text()").extract()
        answer = "".join(answer)[10:].strip()
        answer = re.sub(r'\s+', ' ', answer)
        #answer = [em.strip() for em in answer]
        if answer :
            #print answer
            print answer
            item['answer_content'] = answer



class QuestionSpider(CrawlSpider):
    name = "question_posts"
    allowed_domains = ['www.healthtap.com']
    
    item_count = 0
    close_down = False

    start_urls = [
        #"https://www.healthtap.com/user_questions/44318",
        #"https://www.healthtap.com/topics/Depression",
        #"https://www.healthtap.com/topics/Asthma",
        "https://www.healthtap.com/topics/Arthritis",
    ]

    rules = (
        Rule(LinkExtractor(allow=r"/user_questions/*"),
        callback = "parse_question", follow = True),
    )
    
    def parse_question(self, response):
        
        if self.item_count >= 10000:
            self.close_down = True

        if self.close_down:
            raise CloseSpider(reason = 'Data Filled')

        item = QuestionItem()
        self.get_qid(response, item)
        self.get_qcontent(response, item)
        self.item_count = self.item_count + 1

        yield item
    
    def get_qid(self, response, item):
        qid = response.url.strip().split('/')[-1]
        print "question_id:" + qid
        if qid:
            item['question_id'] = qid
    
    #def get_uid(self, response, item):


    def get_qcontent(self, response, item):    
        qcontent = response.xpath("//*[@class='question-text']/text()").extract()
        if qcontent :
            #print "qcontent :" +qcontent[1].strip().encode('utf-8')
            item['question_content'] = qcontent[1].strip()












