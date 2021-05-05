import scrapy
import re
from scrapy import signals
from pydispatch import dispatcher
from scrapy.http import FormRequest
from scrapy.http import Request
import pandas as pd
import time
from scrapy.utils.response import open_in_browser
from scrapy.shell import inspect_response
from itemadapter import ItemAdapter
import json
#Declare variables to be exported
company_country = []
company_email = []
company_name = []
no_of_employees = []
address = []
company_phone = []
company_contact_person = []
company_website = []
contact_person_name = []
contact_person2_name = []
contact_person3_name = []
contact_person4_name = []
contact_person_title = []
contact_person2_title = []
contact_person3_title = []
contact_person4_title = []
contact_person_phone = []
contact_person2_phone = []
contact_person3_phone = []
contact_person4_phone = []
contact_person_email = []
contact_person2_email = []
contact_person3_email = []
contact_person4_email = []
company_contact_person_title = []
PAGES = [
    
    "https://www.jctrans.net/company/list-0-0-australia-0-3-0-0-0-1.html",
    "https://www.jctrans.net/company/list-0-0-australia-0-3-0-0-0-2.html",
    "https://www.jctrans.net/company/list-0-0-australia-0-3-0-0-0-3.html",
    "https://www.jctrans.net/company/list-0-0-australia-0-3-0-0-0-4.html",
    "https://www.jctrans.net/company/list-0-0-australia-0-3-0-0-0-5.html",
    "https://www.jctrans.net/company/list-0-0-australia-0-3-0-0-0-6.html",
    "https://www.jctrans.net/company/list-0-0-australia-0-3-0-0-0-7.html",
    "https://www.jctrans.net/company/list-0-0-australia-0-3-0-0-0-8.html",
    "https://www.jctrans.net/company/list-0-0-australia-0-3-0-0-0-9.html",
    "https://www.jctrans.net/company/list-0-0-australia-0-3-0-0-0-10.html",
    "https://www.jctrans.net/company/list-0-0-australia-0-3-0-0-0-11.html",
    "https://www.jctrans.net/company/list-0-0-australia-0-3-0-0-0-12.html",
    "https://www.jctrans.net/company/list-0-0-australia-0-3-0-0-0-13.html",
    "https://www.jctrans.net/company/list-0-0-australia-0-3-0-0-0-14.html",
    "https://www.jctrans.net/company/list-0-0-australia-0-3-0-0-0-15.html",
    "https://www.jctrans.net/company/list-0-0-australia-0-3-0-0-0-16.html",

    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-1.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-2.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-3.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-4.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-5.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-6.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-7.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-8.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-9.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-10.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-11.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-12.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-13.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-14.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-15.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-16.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-17.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-18.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-19.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-20.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-21.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-22.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-23.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-24.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-25.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-26.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-27.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-28.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-29.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-30.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-31.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-32.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-33.html",
    "https://www.jctrans.net/company/list-0-0-malaysia-0-3-0-0-0-34.html",
    
    "https://www.jctrans.net/company/list-0-0-new%20zealand-0-3-0-0-0-1.html",
    "https://www.jctrans.net/company/list-0-0-new%20zealand-0-3-0-0-0-2.html",

    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-1.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-2.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-3.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-4.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-5.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-6.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-7.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-8.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-9.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-10.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-11.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-12.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-13.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-14.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-15.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-16.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-17.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-18.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-19.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-20.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-21.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-22.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-23.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-24.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-25.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-26.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-27.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-28.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-29.html",
    "https://www.jctrans.net/company/list-0-0-singapore-0-3-0-0-0-30.html",



]
class JCTransSpider(scrapy.Spider): #neiw
    name = "jctrans"
    start_urls = ['https://www.jctrans.net/Login/Login.html',]
       
        
#SPIDER START      
    #Loop through directory listings
    def parse(self, response):
        form_data = {"UserName":"Vicasso","PassWord":"Vicasso","Remember":"0"}
        headers = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                    'Connection': 'keep-alive',
                    'X-Requested-With': 'XMLHttpRequest',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
                    'Origin': 'https://www.jctrans.net',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Dest': 'empty',
                    'Referer': 'https://www.jctrans.net/Login/Login.html',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'sec-ch-ua-mobile': '?0',
                    'Accept': '*/*',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
                    
                    }
        print(json.dumps(form_data))
        yield scrapy.FormRequest(
                            url='https://www.jctrans.net/Login/SubmitLogin',
                            method='POST',
                            headers=headers,
                            formdata = form_data,
                            callback=self.parse_after_login,
                            )
                            
    
    def parse_after_login(self, response):
        for url in PAGES:
            yield scrapy.Request(url, callback=self.parse_page)

    def parse_page(self, response):
        SET_SELECTOR = 'div.left_contenty > div > div > div.col-md-7.center > div.titlel > a::attr(href)'
        yield from response.follow_all(response.css(SET_SELECTOR), self.parse_listing)

        
    #Find information, append to array
    def parse_listing(self, response):
        print("DETECTED: " + str(response.css('#navright > div.link_login.entry > a::text').extract()) + " BUTTON IN COMPANY PAGE")
        # open_in_browser(response)
        COMPANY_COUNTRY_SELECTOR = '//*[@id="home"]/div[1]/div[2]/div[2]/div[1]/div[2]//text()'
        
        COMPANY_SELECTOR = 'div.titlel::text'
        no_of_employees_SELECTOR = '//*[@id="home"]/div/div/div/div/div[contains(string(),"Number of Employees:")]/following-sibling::div[1]/node()[self::text()]'
        ADDRESS_SELECTOR = '//*[@id="home"]/div[1]/div[2]/div[2]/div[2]/div[2]//text()'
        
        COMPANY_CONTACT_PERSON_SELECTOR = '//*[@id="home"]/div/div[1]/div/div/div//text()'
        COMPANY_CONTACT_PERSON_TITLE_SELECTOR = '//*[@id="home"]/div/div[1]/div/div/div/div[contains(string(),"Job Title:")]/following-sibling::div[1]/node()[self::text()]'
        COMPANY_CONTACT_NUMBER_SELECTOR = '//*[@id="home"]/div/div[1]/div/div/div/div[contains(string(),"Tel:")]/following-sibling::div[1]/node()[self::text()]'
        COMPANY_WEBSITE_SELECTOR = '//*[@id="home"]/div/div/div/div/div[contains(string(),"Website:")]/following-sibling::div[1]/node()[self::text()]'
        COMPANY_EMAIL_SELECTOR = '//*[@id="home"]/div/div[1]/div/div/div/div[contains(string(),"E-mall:")]/following-sibling::div[1]/node()[self::text()]'
        COMPANY_LINKEDIN_SELECTOR = '#home > div.tab-p.kly > div > div.zlf > div.Follow > ul > li.tj4 > a::attr(href)'


        company_country = response.xpath(COMPANY_COUNTRY_SELECTOR).extract()
        company_name = response.css(COMPANY_SELECTOR).extract()
        no_of_employees = response.xpath(no_of_employees_SELECTOR).extract()
        address = response.xpath(ADDRESS_SELECTOR).extract()


        company_phone = response.xpath(COMPANY_CONTACT_NUMBER_SELECTOR).extract()
        company_contact_person = response.xpath(COMPANY_CONTACT_PERSON_SELECTOR).extract_first()
        company_contact_person_title = response.xpath(COMPANY_CONTACT_PERSON_TITLE_SELECTOR).extract()
        company_website = response.xpath(COMPANY_WEBSITE_SELECTOR).extract()
        company_email = response.xpath(COMPANY_EMAIL_SELECTOR).extract()
        company_linkedin = response.css(COMPANY_LINKEDIN_SELECTOR).extract()
        # #Contact Person Loop
        contact_loop_ctr = 1

        while(contact_loop_ctr <= 4):
            
            CONTACT_PERSON_NAME_SELECTOR = '//*[@id="home"]/div[2]/div[2]/div[2]/div['+str(contact_loop_ctr)+']/div[1]//text()'
            CONTACT_PERSON_TITLE_SELECTOR = '#home > div.tab-p.kly > div.zlp.jku > div.zlf > div:nth-child('+ str(contact_loop_ctr)+') > div:nth-child(2) > div.lj.xv::text'
            CONTACT_PERSON_PHONE_SELECTOR = '#home > div.tab-p.kly > div.zlp.jku > div.zlf > div:nth-child('+ str(contact_loop_ctr)+') > div:nth-child(3) > div.lj.xv::text'
            CONTACT_PERSON_EMAIL_SELECTOR = '#home > div.tab-p.kly > div.zlp.jku > div.zlf > div:nth-child('+ str(contact_loop_ctr)+') > div:nth-child(4) > div.lj.xv::text'

            if(contact_loop_ctr == 1):
                contact_person_name = response.xpath(CONTACT_PERSON_NAME_SELECTOR).extract()
                contact_person_title = response.css(CONTACT_PERSON_TITLE_SELECTOR).extract()
                contact_person_phone = response.css(CONTACT_PERSON_PHONE_SELECTOR).extract()
                contact_person_email = response.css(CONTACT_PERSON_EMAIL_SELECTOR).extract()
                
            elif(contact_loop_ctr == 2):
                contact_person2_name = response.xpath(CONTACT_PERSON_NAME_SELECTOR).extract()
                contact_person2_title = response.css(CONTACT_PERSON_TITLE_SELECTOR).extract()
                contact_person2_phone = response.css(CONTACT_PERSON_PHONE_SELECTOR).extract()
                contact_person2_email = response.css(CONTACT_PERSON_EMAIL_SELECTOR).extract()
            elif(contact_loop_ctr == 3):
                contact_person3_name = response.xpath(CONTACT_PERSON_NAME_SELECTOR).extract()
                contact_person3_title = response.css(CONTACT_PERSON_TITLE_SELECTOR).extract()
                contact_person3_phone = response.css(CONTACT_PERSON_PHONE_SELECTOR).extract()
                contact_person3_email = response.css(CONTACT_PERSON_EMAIL_SELECTOR).extract()      
            elif(contact_loop_ctr == 4):
                contact_person4_name = response.xpath(CONTACT_PERSON_NAME_SELECTOR).extract()
                contact_person4_title = response.css(CONTACT_PERSON_TITLE_SELECTOR).extract()
                contact_person4_phone = response.css(CONTACT_PERSON_PHONE_SELECTOR).extract()
                contact_person4_email = response.css(CONTACT_PERSON_EMAIL_SELECTOR).extract()            
            
            contact_loop_ctr+=1
        yield{
            "company_country": company_country,
            "company_name": company_name,
            "no_of_employees": no_of_employees,
            "address":address,
            "company_phone":company_phone,
            "company_contact_person":company_contact_person,
            "company_contact_person_title" : company_contact_person_title,
            "company_website":company_website,
            "company_email":company_email,
            "company_linkedin":company_linkedin,
            "contact_person_name": contact_person_name,
            "contact_person_title": contact_person_title,
            "contact_person_phone": contact_person_phone,
            "contact_person_email": contact_person_email,
            "contact_person2_name": contact_person2_name,
            "contact_person2_title": contact_person2_title,
            "contact_person2_phone": contact_person2_phone,
            "contact_person2_email": contact_person2_email,
            "contact_person3_name": contact_person3_name,
            "contact_person3_title": contact_person3_title,
            "contact_person3_phone": contact_person3_phone,
            "contact_person3_email": contact_person3_email,
            "contact_person4_name": contact_person4_name,
            "contact_person4_title": contact_person4_title,
            "contact_person4_phone": contact_person4_phone,
            "contact_person4_email": contact_person4_email,
            
        }
            
            
    
            
#EOF