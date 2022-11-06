# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RcethItem(scrapy.Item):
    trade_name = scrapy.Field()
    international_name = scrapy.Field()
    dosage_form = scrapy.Field()
    manufacturer = scrapy.Field()
    applicant = scrapy.Field()
    number_of_certificate = scrapy.Field()
    registration_date = scrapy.Field()
    validity = scrapy.Field()
    original = scrapy.Field()
    link_of_instruction = scrapy.Field()
    
    composition = scrapy.Field()
    ATC_code = scrapy.Field()
    prescribed = scrapy.Field()
    storage_list = scrapy.Field()
    term_of_usage = scrapy.Field()
    
