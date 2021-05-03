# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    copmany_country = scrapy.Field()
    company_name = scrapy.Field()
    branch_name = scrapy.Field()
    address =  scrapy.Field()
    company_phone = scrapy.Field()
    company_fax = scrapy.Field()
    company_website = scrapy.Field()
    company_email = scrapy.Field()
    contact_person_name =  scrapy.Field()
    contact_person_title =  scrapy.Field()
    contact_person_phone =  scrapy.Field()
    contact_person_email =  scrapy.Field()
    contact_person2_name =  scrapy.Field()
    contact_person2_title = scrapy.Field()
    contact_person2_phone = scrapy.Field()
    contact_person2_email = scrapy.Field()
    contact_person3_name =  scrapy.Field()
    contact_person3_title = scrapy.Field()
    contact_person3_phone = scrapy.Field()
    contact_person3_email = scrapy.Field()
    contact_person4_name =  scrapy.Field()
    contact_person4_title = scrapy.Field()
    contact_person4_phone = scrapy.Field()
    contact_person4_email = scrapy.Field()
    pass
