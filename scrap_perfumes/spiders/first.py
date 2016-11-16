# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,  Rule
# from scrapy.contrib.linextractors import LinkExtractor
from scrapy.http import Request
from scrap_perfumes.items import ScrapPerfumesItem

class FirstSpider(scrapy.Spider):
    name = "first"
    allowed_domains = ["www.bathandbodyworks.com"]
    start_urls = ['http://www.bathandbodyworks.com/family/index.jsp?categoryId=69342266&cm_sp=LN-_-Perfume+-_-Men\'s&cp=12586965.12587148']


    def parse(self, response):
        for section in response.css('div.hproduct'):
              yield{'source url': section.css('img.photo::attr(src)' ).extract_first(),
                    'fragrance': section.css('div.productFragrance::text').extract(),
                    'product name' : section.css('div.productName.name::text').extract(),
                    'description':section.css('div.short-description::text').extract(),
                    'price':section.css('span.value.price::text').extract(),
                    'gender':'men'
                    }
