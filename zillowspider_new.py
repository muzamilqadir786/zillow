# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
import json
from lxml.html import fromstring
import math
from zillow.items import ZillowItem
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml.html import fromstring
from selenium.webdriver.chrome.options import Options

class ZillowspiderSpider(scrapy.Spider):
    # name = "zillowspider"
    allowed_domains = ["zillow.com"]
    start_urls = (
        # 'http://www.zillow.com/',
        # 'http://www.zillow.com/search/GetResults.htm?spt=homes&status=100000&lt=010000&ht=111111&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=,&yr=,&pho=0&pets=0&parking=0&laundry=0&pnd=0&red=0&zso=0&att=renovated&days=any&ds=all&pmf=0&pf=0&zoom=5&rect=-110972901,41779504,-89527588,46596618&p=1&sort=days&search=map&disp=1&rid=52&rt=2&listright=true&isMapSearch=true&zoom=5',
        # 'http://www.zillow.com/search/GetResults.htm?spt=homes&status=100000&lt=010000&ht=111111&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=,&yr=,&pho=0&pets=0&parking=0&laundry=0&pnd=0&red=0&zso=0&att=renovated&days=any&ds=all&pmf=0&pf=0&zoom=6&rect=-91126099,36496389,-80403443,39151362&p=1&sort=days&search=map&disp=1&rid=24&rt=2&listright=true&isMapSearch=true&zoom=6',
        # 'http://www.zillow.com/search/GetResults.htm?spt=homes&status=100000&lt=010000&ht=111111&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=,&yr=,&pho=0&pets=0&parking=0&laundry=0&pnd=0&red=0&zso=0&att=renovated&days=any&ds=all&pmf=0&pf=0&zoom=5&rect=-109039307,35844534,-87593995,41104190&p=1&sort=days&search=map&disp=1&rid=23&rt=2&listright=true&isMapSearch=true&zoom=5',
        # 'http://www.zillow.com/search/GetResults.htm?spt=homes&status=100000&lt=010000&ht=111111&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=,&yr=,&pho=0&pets=0&parking=0&laundry=0&pnd=0&red=0&zso=0&att=renovated&days=any&ds=all&pmf=0&pf=0&zoom=5&rect=-109434815,32537551,-87989502,38022131&p=1&sort=days&search=map&disp=1&rid=45&rt=2&listright=true&isMapSearch=true&zoom=5',
        # 'http://www.zillow.com/search/GetResults.htm?spt=homes&status=100000&lt=010000&ht=111111&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=,&yr=,&pho=0&pets=0&parking=0&laundry=0&pnd=0&red=0&zso=0&att=renovated&days=any&ds=all&pmf=0&pf=0&zoom=7&rect=-75440369,40886524,-70079041,42145078&p=1&sort=days&search=map&disp=1&rid=11&rt=2&listright=true&isMapSearch=true&zoom=7',
        # 'http://www.zillow.com/search/GetResults.htm?spt=homes&status=100000&lt=010000&ht=111111&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=,&yr=,&pho=0&pets=0&parking=0&laundry=0&pnd=0&red=0&zso=0&att=renovated&days=any&ds=all&pmf=0&pf=0&zoom=8&rect=143447113,13035331,146127777,13852747&p=1&sort=days&search=map&disp=1&rid=17&rt=2&listright=true&isMapSearch=true&zoom=8',
        # 'http://www.zillow.com/search/GetResults.htm?spt=homes&status=100000&lt=010000&ht=111111&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=,&yr=,&pho=0&pets=0&parking=0&laundry=0&pnd=0&red=0&zso=0&att=renovated&days=any&ds=all&pmf=0&pf=0&zoom=5&rect=-110401612,38950865,-88956299,43984910&p=1&sort=days&search=map&disp=1&rid=38&rt=2&listright=true&isMapSearch=true&zoom=5',
        # 'http://www.zillow.com/search/GetResults.htm?spt=homes&status=100000&lt=010000&ht=111111&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=,&yr=,&pho=0&pets=0&parking=0&laundry=0&pnd=0&red=0&zso=0&att=renovated&days=any&ds=all&pmf=0&pf=0&zoom=6&rect=-85248414,33838482,-74525757,36584657&p=1&sort=days&search=map&disp=1&rid=36&rt=2&listright=true&isMapSearch=true&zoom=6',
        'http://www.zillow.com/search/GetResults.htm?spt=homes&status=100000&lt=111101&ht=111111&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=,&yr=,&pho=0&pets=0&parking=0&laundry=0&pnd=0&red=0&zso=0&att=Renovated&days=any&ds=all&pmf=0&pf=0&zoom=6&rect=-78206177,38698372,-71240845,41586688&p=1&sort=featured&search=maplist&disp=1&rid=40&rt=2&listright=true&isMapSearch=true&zoom=6',
        # 'http://www.zillow.com/search/GetResults.htm?spt=homes&status=100000&lt=010000&ht=111111&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=,&yr=,&pho=0&pets=0&parking=0&laundry=0&pnd=0&red=0&zso=0&att=renovated&days=any&ds=all&pmf=0&pf=0&zoom=4&rect=-127463379,28478348,-84572754,39588757&p=1&sort=days&search=map&disp=1&rid=41&rt=2&listright=true&isMapSearch=true&zoom=4',
        # 'http://www.zillow.com/search/GetResults.htm?spt=homes&status=100000&lt=010000&ht=111111&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=,&yr=,&pho=0&pets=0&parking=0&laundry=0&pnd=0&red=0&zso=0&att=renovated&days=any&ds=all&pmf=0&pf=0&zoom=6&rect=-80084839,38852542,-69362183,41438608&p=1&sort=days&search=maplist&disp=1&rid=40&rt=2&listright=true&isMapSearch=true&zoom=6',
        # 'http://www.zillow.com/search/GetResults.htm?spt=homes&status=100000&lt=010000&ht=111111&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=,&yr=,&pho=0&pets=0&parking=0&laundry=0&pnd=0&red=0&zso=0&att=renovated&days=any&ds=all&pmf=0&pf=0&zoom=5&rect=-118267823,40505446,-96822510,45452424&p=1&sort=days&search=maplist&disp=1&rid=62&rt=2&listright=true&isMapSearch=true&zoom=5',
        # # 'http://www.zillow.com/search/GetResults.htm?spt=homes&status=100000&lt=010000&ht=111111&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=,&yr=,&pho=0&pets=0&parking=0&laundry=0&pnd=0&red=0&zso=0&att=renovated&days=any&ds=all&pmf=0&pf=0&zoom=5&rect=-90911865,36244273,-69466553,41508577&p=1&sort=days&search=maplist&disp=1&rid=61&rt=2&listright=true&isMapSearch=true&zoom=5',
    )

    base_url = 'http://www.zillow.com'

    def parse(self, response):
        opts = Options()
        opts.binary_location = '/usr/bin/chromium-browser'
        driver = webdriver.Chrome(chrome_options=opts)
        driver.get('http://www.google.com')

        jsonresponse = json.loads(response.body_as_unicode())
        pages = jsonresponse["list"]["pagination"]
        total_count = jsonresponse["list"]["binCounts"]["totalResultCount"]
        print total_count

        print pages
        pages_html = fromstring(pages)
        pages = pages_html.xpath('//li/a/@href')
        print len(pages)
        page_url = pages[0]
        print page_url


        import sys
        # sys.exit(1)
    #     for page_no in range(1,int(math.ceil(total_count/25.0))+1):
    #         page_url = page_url.rsplit('/',2)[0]
    #         print page_url
    #         break
    #         # page_url = '{0}/0_mmm/{1}_p/'.format(page_url,page_no)
    #         # page_url = '{0}/{1}_p/'.format(page_url,page_no)
    #         # print self.base_url+page_url
    #         # sys.exit(1)
    #         # time.sleep(1)
    #         # yield Request(self.base_url+page_url,self.get_links,dont_filter=True)
    #
    # def get_links(self, response):
    #     print "here in get"
    #     hxs = Selector(response)
    #     property_urls = hxs.xpath('//a[@class="hdp-link routable"]/@href').extract()
    #     driver = webdriver.Firefox()
    #     for property_url in property_urls:
    #         driver.get(self.base_url+property_url)
    #         # time.sleep(1)
    #         # yield Request(self.base_url+property_url,self.parse_info,dont_filter=True)
    #
    # # def parse_info(self, response):
    # #     print response.url
    #     # with open('mfile.html','wb') as mf:
    #     #     mf.write(response.body)
    #         hxs = fromstring(driver.page_source)
    #         # hxs = Selector(response)
    #         item = ZillowItem()
    #         item['propertyUrl'] = response.url
    #         # phone = hxs.xpath('//span[@class="snl phone"]/text()').extract()
    #         phone = hxs.xpath('//span[contains(text(),"Property Owner")]/following-sibling::span[@class="snl phone"]/text()')
    #         print phone
    #         if phone:
    #             item['ownerPhone'] = phone[-1]
    #             print phone
    #
    #         price = hxs.xpath('normalize-space(//div[@class="main-row  home-summary-row"]/span/text())')
    #         if price:
    #             item['price'] = price
    #
    #         # zestimate = hxs.xpath('//span[conatins(text(),"Zestimate")]/following-sibling::span[1]/text()').extract()
    #         zestimate = hxs.xpath('normalize-space(//div[@class="  home-summary-row"]/span[2]/text())')
    #         if zestimate:
    #             item['zestimate'] = zestimate
    #
    #         city_state_zip = hxs.xpath('//span[@class="zsg-h2 addr_city"]/text()')
    #         if city_state_zip:
    #             print city_state_zip
    #             city_state_zip = city_state_zip[0].split(',')
    #             city = city_state_zip[0]
    #             state_zip = city_state_zip[1].strip().split()
    #             if state_zip:
    #                 print state_zip
    #                 state = state_zip[0]
    #                 zipcode = state_zip[1]
    #                 item['state'] = state
    #                 item['zipcode'] = zipcode
    #
    #             item['city'] = city
    #
    #         street = hxs.xpath('//header[@class="zsg-content-header addr"]/h1/text()')
    #         if street:
    #             item['street'] = street[0].rstrip(', ')
    #
    #
    #         beds_baths_sqfts = hxs.xpath('//span[@class="addr_bbs"]/text()')
    #         if len(beds_baths_sqfts) == 3:
    #             item['beds'], item['baths'], item['sqfts'] = beds_baths_sqfts
    #
    #         price_history = hxs.xpath('//h2[contains(text(),"Price History")]/following-sibling::table[1]')
    #         ptheaders = price_history.xpath('./thead/tr/th/text()')
    #         ptrows = price_history.xpath('./tbody/tr')
    #         for ptrow in ptrows:
    #             item['priceHistory'] = str(dict(zip(ptheaders,ptrow)))
    #             print "in loop"
    #
    #         yield item

        # print price_history
        # elif len(beds_baths_sqfts) == 2:
        #     item

        # print item
        # yield  item




