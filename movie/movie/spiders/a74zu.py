# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider


class A74zuSpider(RedisCrawlSpider):
    name = '74zu'
    allowed_domains = ['74zu.com']
    # start_urls = ['http://www.74zu.com/type/1.html']
    redis_key = '74zu:start_urls'

    rules = (
        Rule(LinkExtractor(restrict_xpaths='/html/body/div[2]/div[2]/div/div'), follow=True, callback='parse_item'),
        # Rule(LinkExtractor(restrict_xpaths='/html/body/div[2]/div/div/div[4]/div/ul/li'), callback='parse_link'),
        Rule(LinkExtractor(restrict_xpaths='/html/body/div[2]/div[3]'), follow=True),
    )

    def parse_item(self, response):
        item = {}
        item['name'] = response.xpath('/html/body/div[2]/div/div/div[1]/h1/text()').extract_first()
        item['director'] = response.xpath('/html/body/div[2]/div/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/text()').extract_first()
        item['actors'] = response.xpath('//*[@id="casts"]/text()').extract_first()
        item['country'] = response.xpath('/html/body/div[2]/div/div/div[2]/div[1]/div[2]/table/tbody/tr[4]/td[2]/text()').extract_first()
        item['language'] = response.xpath('/html/body/div[2]/div/div/div[2]/div[1]/div[2]/table/tbody/tr[5]/td[2]/text()').extract_first()
        item['release_date'] = response.xpath('/html/body/div[2]/div/div/div[2]/div[1]/div[2]/table/tbody/tr[6]/td[2]/text()').extract_first()
        item['score'] = response.xpath('/html/body/div[2]/div/div/div[2]/div[1]/div[2]/table/tbody/tr[7]/td[2]/a/text()').extract_first()
        item['intro'] = response.xpath('/html/body/div[2]/div/div/div[2]/div[1]/div[2]/p[2]/text()').extract_first().strip()
        item['play_url'] = response.urljoin(response.xpath('/html/body/div[2]/div/div/div[4]/div/ul/li/a/@href').extract_first())

        yield scrapy.Request(item['play_url'], callback=self.parse_link, meta={'item': item})

    def parse_link(self, response):
        item = response.meta['item']
        item['play_link'] = response.xpath('//*[@id="player"]/iframe/@src').extract_first()

        print(item)
        yield item