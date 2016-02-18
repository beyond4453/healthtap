#encoding: utf-8

import scrapy
import re
from scrapy.selector import Selector
from users.items import UsersItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.exceptions import CloseSpider


class UserSpider(scrapy.Spider):
    
    name = "users"
    intro_flag = False
    #item_count = 0
    
    allowed_domains = ['www.healthtap.com']
    
    f = open("urls_uid.txt")
    start_urls = [ url.strip() for url in f.readlines()  ]
    f.close()

    '''
    rules = (
        Rule(LinkExtractor(allow=r"/experts/\d"),
        callback = "parse_user", follow = True),
    )
    '''

    def parse(self, response):
        '''
        if self.item_count >= 10:
            raise CloseSpider(reason = "API usage exceeded")
        '''
        
        self.intro_flag = False
        item = UsersItem()
        
        self.get_uid(response, item)
        self.get_uname(response, item)
        
        self.get_uintro(response, item)
        self.get_uexp(response, item)

        self.get_uspecialty(response, item)
        self.get_uaddr(response, item)
        self.get_uedu(response, item)
        self.get_ufollow(response, item)
        self.get_uinterest(response, item)
        
        self.get_usaved(response, item)
        self.get_uhelped(response, item)
        self.get_uagrees(response, item)
        self.get_uthanks(response, item)
        self.get_recommends(response, item)
        #self.get_ustars(response, item)

        #self.item_count = self.item_count + 1
        #print self.item_count 

        yield item
        
    def get_uid(self, response, item):
        uid = response.xpath("//div[@class='doctor-header']/@data-doctor-id").extract()
        uid = uid[0]
        if uid :
            item['user_id'] = uid

    def get_uintro(self, response, item):
        uintro = response.xpath("//div[@class='about-item'][1]/div[2]/div/text()").extract()
        uintro = "".join(uintro).strip()
        uintro = uintro.replace(u"\u00a0"," ")
        uintro = re.sub(r'\s+', ' ', uintro) 
        if uintro:
            self.intro_flag = True
            item["user_intro"] = uintro
    
    
    def get_uexp(self, response, item):
        if self.intro_flag:
            uexp = response.xpath("//div[@class='about-item'][3]/div[2]/text()").extract()
            uexp = uexp[0].strip().replace('\n', '')
            #somepeple didnt have a proper exp,
            uexp = re.sub(r'[A-Z][a-zA-Z ]*', '' , uexp)
            if uexp:
                item["user_exp"] = uexp
                self.intro_flag = False
        else :
            uexp = response.xpath("//div[@class='about-item'][2]/div[2]/text()").extract()
            uexp = uexp[0].strip().replace('\n', '')
            uexp = re.sub(r'[A-Z][a-zA-Z ]*', '' , uexp)
            if uexp:
                item["user_exp"] = uexp
                self.intro_flag = False
        
    
    def get_uaddr(self, response, item):
        uaddr = response.xpath("//div[@class='location-content'][1]/div[1]//text()").extract()
        uaddr = "".join(uaddr).strip()
        uaddr = re.sub(r'\s+',' ', uaddr)
        if uaddr:
            #print uaddr
            item["user_address"] = uaddr
    
    def get_uedu(self, response, item):
        uedu = response.xpath("//div[@class='about-item education']/div[2]/div/text()").extract()
        uedu = "".join(uedu).strip()
        uedu = re.sub(r'\s+', ' ', uedu)
        if uedu:
            #print uedu
            item["user_edu"] = uedu



    def get_uname(self, response, item):
        uname = response.xpath("//div[@class='main-doc-description']/h1/span/text()").extract()
        #uname = info[0].split(',')[0]
        if uname:
            #print uname
            #print "doctor_name:" + "".join(uname)
            item['user_name'] = "".join(uname).strip()
    

    def get_uspecialty(self, response, item):
        uspecialty = response.xpath("//div[@class='main-doc-description']/div[2]/text()").extract()
        if uspecialty:
            #print uspecialty
            item['user_specialty'] = uspecialty[0].strip()
    
    def get_uinterest(self, response, item):
        uinterest = response.xpath("//div[@class='known-for-container']/a/text()").extract()
        #each element in the list use the strip() function
        uinterest = [x.strip() for x in uinterest]
        if uinterest:
            #print uinterest
            item['user_interest'] = uinterest


    def get_ufollow(self, response, item):
        ufollow = response.xpath("//div[@class='doctor-item doctor-result']/@doctor_id").extract()
        if ufollow:
            #print ufollow
            item['user_followed'] = ufollow


    def get_usaved(self, response, item):
        usaved = response.xpath("//div[@class='saved-icon']/../span/text()").extract()
        usaved = "".join(usaved).strip()
        if usaved :
            #print usaved
            item['user_saved'] = usaved

    def get_uhelped(self, response, item):
        uhelped = response.xpath("//div[@class='helped-icon']/../span/text()").extract()
        uhelped = "".join(uhelped).strip()
        if uhelped :
            item['user_helped'] = uhelped

    def get_uagrees(self, response, item):
        uagrees = response.xpath("//div[@class='agrees-icon']/../span/text()").extract()
        uagrees = "".join(uagrees).strip()
        if uagrees :
            item['user_agrees'] = uagrees

    def get_uthanks(self, response, item):
        uthanks = response.xpath("//div[@class='thanks-icon']/../span/text()").extract()
        uthanks = "".join(uthanks).strip()
        if uthanks :
            item['user_thanks'] = uthanks

    def get_recommends(self, response, item):
        urecommends = response.xpath("//div[@class='testimonial-note']/text()").extract()
        #urecommends = "".join(urecommends).strip()
        #urecommends = map(lambda it : it.strip, urecommends)
        urecommends = [str(x).strip() for x in urecommends]
        if urecommends :
            item['user_recommends'] = urecommends





