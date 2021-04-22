import scrapy
import re
from scrapy import signals
from pydispatch import dispatcher
from scrapy.http import FormRequest
import pandas as pd
import time
from scrapy.utils.response import open_in_browser
from scrapy.shell import inspect_response

#Declare variables to be exported
company_country = []
company_email = []
company_name = []
branch_name = []
address = []
company_phone = []
company_fax = []
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
PAGES = [
            #AU
            'https://www.wcaworld.com/Directory?siteID=24&au=m&pageIndex=1&pageSize=100&searchby=CountryCode&country=AU&city=&keyword=&orderby=CountryCity&networkIds=1&networkIds=2&networkIds=3&networkIds=4&networkIds=61&networkIds=98&networkIds=108&networkIds=5&networkIds=22&networkIds=13&networkIds=18&networkIds=15&networkIds=16&networkIds=38&networkIds=103&layout=v1&submitted=search',
            #NZ
            'https://www.wcaworld.com/Directory?siteID=24&au=m&pageIndex=1&pageSize=100&searchby=CountryCode&country=NZ&city=&keyword=&orderby=CountryCity&networkIds=1&networkIds=2&networkIds=3&networkIds=4&networkIds=61&networkIds=98&networkIds=108&networkIds=5&networkIds=22&networkIds=13&networkIds=18&networkIds=15&networkIds=16&networkIds=38&networkIds=103&layout=v1&submitted=search',
            #CN
            'https://www.wcaworld.com/Directory/NextV1?networkId=&siteID=24&au=m&pageIndex=1&pageSize=100&searchby=CountryCode&country=CN&city=&keyword=&orderby=CountryCity&networkIds=1&networkIds=2&networkIds=3&networkIds=4&networkIds=61&networkIds=98&networkIds=108&networkIds=5&networkIds=22&networkIds=13&networkIds=18&networkIds=15&networkIds=16&networkIds=38&networkIds=103&layout=v1&submitted=search&lastCid=0&&_=1618814505701',
            'https://www.wcaworld.com/Directory/NextV1?networkId=&siteID=24&au=m&pageIndex=2&pageSize=100&searchby=CountryCode&country=CN&city=&keyword=&orderby=CountryCity&networkIds=1&networkIds=2&networkIds=3&networkIds=4&networkIds=61&networkIds=98&networkIds=108&networkIds=5&networkIds=22&networkIds=13&networkIds=18&networkIds=15&networkIds=16&networkIds=38&networkIds=103&layout=v1&submitted=search&lastCid=0&&_=1618814505702',
            'https://www.wcaworld.com/Directory/NextV1?networkId=&siteID=24&au=m&pageIndex=3&pageSize=100&searchby=CountryCode&country=CN&city=&keyword=&orderby=CountryCity&networkIds=1&networkIds=2&networkIds=3&networkIds=4&networkIds=61&networkIds=98&networkIds=108&networkIds=5&networkIds=22&networkIds=13&networkIds=18&networkIds=15&networkIds=16&networkIds=38&networkIds=103&layout=v1&submitted=search&lastCid=0&&_=1618814505703',
            'https://www.wcaworld.com/Directory/NextV1?networkId=&siteID=24&au=m&pageIndex=4&pageSize=100&searchby=CountryCode&country=CN&city=&keyword=&orderby=CountryCity&networkIds=1&networkIds=2&networkIds=3&networkIds=4&networkIds=61&networkIds=98&networkIds=108&networkIds=5&networkIds=22&networkIds=13&networkIds=18&networkIds=15&networkIds=16&networkIds=38&networkIds=103&layout=v1&submitted=search&lastCid=0&&_=1618814505704',
            'https://www.wcaworld.com/Directory/NextV1?networkId=&siteID=24&au=m&pageIndex=5&pageSize=100&searchby=CountryCode&country=CN&city=&keyword=&orderby=CountryCity&networkIds=1&networkIds=2&networkIds=3&networkIds=4&networkIds=61&networkIds=98&networkIds=108&networkIds=5&networkIds=22&networkIds=13&networkIds=18&networkIds=15&networkIds=16&networkIds=38&networkIds=103&layout=v1&submitted=search&lastCid=0&&_=1618814505705',
            'https://www.wcaworld.com/Directory/NextV1?networkId=&siteID=24&au=m&pageIndex=6&pageSize=100&searchby=CountryCode&country=CN&city=&keyword=&orderby=CountryCity&networkIds=1&networkIds=2&networkIds=3&networkIds=4&networkIds=61&networkIds=98&networkIds=108&networkIds=5&networkIds=22&networkIds=13&networkIds=18&networkIds=15&networkIds=16&networkIds=38&networkIds=103&layout=v1&submitted=search&lastCid=0&&_=1618814505706',
            'https://www.wcaworld.com/Directory/NextV1?networkId=&siteID=24&au=m&pageIndex=7&pageSize=100&searchby=CountryCode&country=CN&city=&keyword=&orderby=CountryCity&networkIds=1&networkIds=2&networkIds=3&networkIds=4&networkIds=61&networkIds=98&networkIds=108&networkIds=5&networkIds=22&networkIds=13&networkIds=18&networkIds=15&networkIds=16&networkIds=38&networkIds=103&layout=v1&submitted=search&lastCid=0&&_=1618814505707',
            'https://www.wcaworld.com/Directory/NextV1?networkId=&siteID=24&au=m&pageIndex=8&pageSize=100&searchby=CountryCode&country=CN&city=&keyword=&orderby=CountryCity&networkIds=1&networkIds=2&networkIds=3&networkIds=4&networkIds=61&networkIds=98&networkIds=108&networkIds=5&networkIds=22&networkIds=13&networkIds=18&networkIds=15&networkIds=16&networkIds=38&networkIds=103&layout=v1&submitted=search&lastCid=0&&_=1618814505708',
            'https://www.wcaworld.com/Directory/NextV1?networkId=&siteID=24&au=m&pageIndex=9&pageSize=100&searchby=CountryCode&country=CN&city=&keyword=&orderby=CountryCity&networkIds=1&networkIds=2&networkIds=3&networkIds=4&networkIds=61&networkIds=98&networkIds=108&networkIds=5&networkIds=22&networkIds=13&networkIds=18&networkIds=15&networkIds=16&networkIds=38&networkIds=103&layout=v1&submitted=search&lastCid=0&&_=1618814505709',
            'https://www.wcaworld.com/Directory/NextV1?networkId=&siteID=24&au=m&pageIndex=10&pageSize=100&searchby=CountryCode&country=CN&city=&keyword=&orderby=CountryCity&networkIds=1&networkIds=2&networkIds=3&networkIds=4&networkIds=61&networkIds=98&networkIds=108&networkIds=5&networkIds=22&networkIds=13&networkIds=18&networkIds=15&networkIds=16&networkIds=38&networkIds=103&layout=v1&submitted=search&lastCid=0&&_=1618814505710',
            'https://www.wcaworld.com/Directory/NextV1?networkId=&siteID=24&au=m&pageIndex=11&pageSize=100&searchby=CountryCode&country=CN&city=&keyword=&orderby=CountryCity&networkIds=1&networkIds=2&networkIds=3&networkIds=4&networkIds=61&networkIds=98&networkIds=108&networkIds=5&networkIds=22&networkIds=13&networkIds=18&networkIds=15&networkIds=16&networkIds=38&networkIds=103&layout=v1&submitted=search&lastCid=0&&_=1618814505711',
            'https://www.wcaworld.com/Directory/NextV1?networkId=&siteID=24&au=m&pageIndex=12&pageSize=100&searchby=CountryCode&country=CN&city=&keyword=&orderby=CountryCity&networkIds=1&networkIds=2&networkIds=3&networkIds=4&networkIds=61&networkIds=98&networkIds=108&networkIds=5&networkIds=22&networkIds=13&networkIds=18&networkIds=15&networkIds=16&networkIds=38&networkIds=103&layout=v1&submitted=search&lastCid=0&&_=1618814505712',
            'https://www.wcaworld.com/Directory/NextV1?networkId=&siteID=24&au=m&pageIndex=13&pageSize=100&searchby=CountryCode&country=CN&city=&keyword=&orderby=CountryCity&networkIds=1&networkIds=2&networkIds=3&networkIds=4&networkIds=61&networkIds=98&networkIds=108&networkIds=5&networkIds=22&networkIds=13&networkIds=18&networkIds=15&networkIds=16&networkIds=38&networkIds=103&layout=v1&submitted=search&lastCid=0&&_=1618814505713',
            'https://www.wcaworld.com/Directory/NextV1?networkId=&siteID=24&au=m&pageIndex=14&pageSize=100&searchby=CountryCode&country=CN&city=&keyword=&orderby=CountryCity&networkIds=1&networkIds=2&networkIds=3&networkIds=4&networkIds=61&networkIds=98&networkIds=108&networkIds=5&networkIds=22&networkIds=13&networkIds=18&networkIds=15&networkIds=16&networkIds=38&networkIds=103&layout=v1&submitted=search&lastCid=0&&_=1618814505714',
            'https://www.wcaworld.com/Directory/NextV1?networkId=&siteID=24&au=m&pageIndex=15&pageSize=100&searchby=CountryCode&country=CN&city=&keyword=&orderby=CountryCity&networkIds=1&networkIds=2&networkIds=3&networkIds=4&networkIds=61&networkIds=98&networkIds=108&networkIds=5&networkIds=22&networkIds=13&networkIds=18&networkIds=15&networkIds=16&networkIds=38&networkIds=103&layout=v1&submitted=search&lastCid=0&&_=1618814505715',
            'https://www.wcaworld.com/Directory/NextV1?networkId=&siteID=24&au=m&pageIndex=18&pageSize=100&searchby=CountryCode&country=CN&city=&keyword=&orderby=CountryCity&networkIds=1&networkIds=2&networkIds=3&networkIds=4&networkIds=61&networkIds=98&networkIds=108&networkIds=5&networkIds=22&networkIds=13&networkIds=18&networkIds=15&networkIds=16&networkIds=38&networkIds=103&layout=v1&submitted=search&lastCid=0&&_=1618814505718',
]
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['https://www.wcaworld.com/Account/Login?']

    #Closing Listener
    def __init__(self):
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    #Spider Closing
    def spider_closed(self, spider):
        scraped_data = pd.DataFrame({
            'country' : company_country,
            'company_name': company_name,
            'branch_name ': branch_name,
            'address' : address,
            'company_phone' : company_phone,
            'company_fax' : company_fax,
            'company_website' : company_website,
            'company_email' : company_email,
            'contact_person_name' : contact_person_name,
            'contact_person_title' : contact_person_title,
            'contact_person_phone' : contact_person_phone,
            'contact_person_email' : contact_person_email,
            'contact_person2_name' : contact_person2_name,
            'contact_person2_title' : contact_person2_title,
            'contact_person2_phone' : contact_person2_phone,
            'contact_person2_email' : contact_person2_email,
            'contact_person3_name' : contact_person3_name,
            'contact_person3_title' : contact_person3_title,
            'contact_person3_phone' : contact_person3_phone,
            'contact_person3_email' : contact_person3_email,
            'contact_person4_name' : contact_person4_name,
            'contact_person4_title' : contact_person4_title,
            'contact_person4_phone' : contact_person4_phone,
            'contact_person4_email' : contact_person4_email,
        })
        scraped_data = scraped_data.replace(regex={r'\[\'': '', r'\']': '', r'\[]': '', r'[^a-zA-Z0-9 @\.\-\+]+': ''})
        scraped_data = scraped_data.replace(regex={r'\[\'': r'\[\' '})
        scraped_data = scraped_data.replace(regex={r'[^a-zA-Z0-9 @\.\-\+]+': ''})
        scraped_data = scraped_data.replace('[]','')
        scraped_data.to_excel("output_final3.xlsx")
        
#SPIDER START      
    #Loop through directory listings
    def parse(self, response):
        csrf_token = response.xpath('//*[@name="__RequestVerificationToken"]/@value').extract_first()
        return scrapy.FormRequest.from_response(response,
                                        formid='login-form',
                                        clickdata={'type': 'submit'},
                                        formdata={
                                                # 'siteID': '24', 
                                                # 'referer': 'https://www.wcaworld.com',
                                                # 'REMOTE_ADDR': '220.133.224.12',
                                                # 'returnurl': '/MemberSection',
                                                # 'verifyurl': 'https://www.wcaworld.com/Account/SsoLoginResult/',
                                                '__RequestVerificationToken': csrf_token,
                                                'username':'goftptw',
                                                'password': '471183',
                                                'rememberme': "1"},
                                        callback=self.parse_after_login)
    
    
    def parse_after_login(self, response):
        if b"Member Section" in response.body:
            self.log("Successfully logged in. Let's start crawling!")
            # Now the crawling can begin..
            for url in PAGES:
                yield scrapy.Request(url, callback=self.parse_page)
        else:
            self.log("Bad times :(")
            # Something went wrong, we couldn't log in, so nothing happens.
           

    def parse_page(self, response):
        print("DETECTED: " + str(response.css('#navright > div.link_login.entry > a::text').extract()) + " BUTTON IN DIRECTORY LISTING PAGE")
        SET_SELECTOR ='#directory_result > div > div.groupHQ > div.directory_search_group > div > ul > li > a::attr(href)'       
        yield from response.follow_all(response.css(SET_SELECTOR), self.parse_listing)

        
    #Find information, append to array
    def parse_listing(self, response):
        print("DETECTED: " + str(response.css('#navright > div.link_login.entry > a::text').extract()) + " BUTTON IN COMPANY PAGE")
        # open_in_browser(response)
        COMPANY_COUNTRY_SELECTOR = '//*[@id="profilepage"]/div/div[4]/div/div/div[2]/div[2]/div/div[1]//text()'
        COMPANY_SELECTOR = '.company::text'
        BRANCH_NAME_SELECTOR = '.branchname::text'
        ADDRESS_SELECTOR = 'div.profile_wrapper > div.row > div > div.profile_headline + span::text'
        COMPANY_CONTACT_NUMBER_SELECTOR = '//*[@id="profilepage"]/div/div/div/div[contains(string(),"Phone:")]/following-sibling::div[1]/node()[self::text()]'
        COMPANY_FAX_NUMBER_SELECTOR = '//*[@id="profilepage"]/div/div/div/div[contains(string(),"Fax:")]/following-sibling::div[1]/node()[self::text()]'
        COMPANY_WEBSITE_SELECTOR = '//*[@id="profilepage"]/div/div/div/div[contains(string(),"Website:")]/following-sibling::div[1]/a/node()[self::text()]'
        COMPANY_EMAIL_SELECTOR = '//*[@id="profilepage"]/div/div/div/div[contains(string(),"Email:")]/following-sibling::div[1]/a//text()'
    
        company_country.append(response.xpath(COMPANY_COUNTRY_SELECTOR).extract())
        company_name.append(response.css(COMPANY_SELECTOR).extract())
        branch_name.append(response.css(BRANCH_NAME_SELECTOR).extract())
        address.append(response.css(ADDRESS_SELECTOR).extract())
        company_phone.append(response.xpath(COMPANY_CONTACT_NUMBER_SELECTOR).extract())
        company_fax.append(response.xpath(COMPANY_FAX_NUMBER_SELECTOR).extract())
        company_website.append(response.xpath(COMPANY_WEBSITE_SELECTOR).extract())
        company_email.append(response.xpath(COMPANY_EMAIL_SELECTOR).extract())

        #Contact Person Loop
        contact_loop_ctr = 2

        while(contact_loop_ctr <= 5):
            CONTACT_PERSON_NAME_SELECTOR = '//*[@id="contactperson"]/div['+str(contact_loop_ctr)+']/div/div/div/div[contains(string(),"Name:")]/following-sibling::div//text()'
            CONTACT_PERSON_TITLE_SELECTOR = '//*[@id="contactperson"]/div['+str(contact_loop_ctr)+']/div/div/div/div[contains(string(),"Title:")]/following-sibling::div//text()'
            CONTACT_PERSON_PHONE_SELECTOR = '//*[@id="contactperson"]/div['+str(contact_loop_ctr)+']/div/div/div/div[contains(string(),"Direct Line")]/following-sibling::div//text()'
            CONTACT_PERSON_EMAIL_SELECTOR = '//*[@id="contactperson"]/div['+str(contact_loop_ctr)+']/div/div/div/div[contains(string(),"Email")]/following-sibling::div//text()'
            #GET RID OF THE FREAKIN SPACES WHY ARE THERE SPACES ANYWAY?!
            if(contact_loop_ctr == 2):
                contact_person_name.append(re.sub('\\\\r\\\\n','',re.sub(' +',' ',str(response.xpath(CONTACT_PERSON_NAME_SELECTOR).extract()))).strip())
                contact_person_title.append(re.sub('\\\\r\\\\n','',re.sub(' +',' ',str(response.xpath(CONTACT_PERSON_TITLE_SELECTOR).extract()))).strip())
                contact_person_phone.append(re.sub('\\\\r\\\\n','',re.sub(' +',' ',str(response.xpath(CONTACT_PERSON_PHONE_SELECTOR).extract()))).strip())
                contact_person_email.append(re.sub('\\\\r\\\\n','',re.sub(' +',' ',str(response.xpath(CONTACT_PERSON_EMAIL_SELECTOR).extract()))).strip())
                
            elif(contact_loop_ctr == 3):
                contact_person2_name.append(re.sub('\\\\r\\\\n','',re.sub(' +',' ',str(response.xpath(CONTACT_PERSON_NAME_SELECTOR).extract()))).strip())
                contact_person2_title.append(re.sub('\\\\r\\\\n','',re.sub(' +',' ',str(response.xpath(CONTACT_PERSON_TITLE_SELECTOR).extract()))).strip())
                contact_person2_phone.append(re.sub('\\\\r\\\\n','',re.sub(' +',' ',str(response.xpath(CONTACT_PERSON_PHONE_SELECTOR).extract()))).strip())
                contact_person2_email.append(re.sub('\\\\r\\\\n','',re.sub(' +',' ',str(response.xpath(CONTACT_PERSON_EMAIL_SELECTOR).extract()))).strip())
            elif(contact_loop_ctr == 4):
                contact_person3_name.append(re.sub('\\\\r\\\\n','',re.sub(' +',' ',str(response.xpath(CONTACT_PERSON_NAME_SELECTOR).extract()))).strip())
                contact_person3_title.append(re.sub('\\\\r\\\\n','',re.sub(' +',' ',str(response.xpath(CONTACT_PERSON_TITLE_SELECTOR).extract()))).strip())
                contact_person3_phone.append(re.sub('\\\\r\\\\n','',re.sub(' +',' ',str(response.xpath(CONTACT_PERSON_PHONE_SELECTOR).extract()))).strip())
                contact_person3_email.append(re.sub('\\\\r\\\\n','',re.sub(' +',' ',str(response.xpath(CONTACT_PERSON_EMAIL_SELECTOR).extract()))).strip())            
            elif(contact_loop_ctr == 5):
                contact_person4_name.append(re.sub('\\\\r\\\\n','',re.sub(' +',' ',str(response.xpath(CONTACT_PERSON_NAME_SELECTOR).extract()))).strip())
                contact_person4_title.append(re.sub('\\\\r\\\\n','',re.sub(' +',' ',str(response.xpath(CONTACT_PERSON_TITLE_SELECTOR).extract()))).strip())
                contact_person4_phone.append(re.sub('\\\\r\\\\n','',re.sub(' +',' ',str(response.xpath(CONTACT_PERSON_PHONE_SELECTOR).extract()))).strip())
                contact_person4_email.append(re.sub('\\\\r\\\\n','',re.sub(' +',' ',str(response.xpath(CONTACT_PERSON_EMAIL_SELECTOR).extract()))).strip())            
            
            contact_loop_ctr+=1
        pass
            
            
    
            
#EOF