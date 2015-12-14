# -*- coding: utf-8 -*-
# /bin/.pythonstartup
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
import simplejson
from lxml.html import fromstring
import math
from zillow.items import ZillowItem
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml.html import fromstring
# from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
import os
import re
import json
class ZillowspiderSpider(scrapy.Spider):
    name = "zillowspider"
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
          'http://www.zillow.com/search/GetResults.htm?spt=homes&status=100000&lt=111101&ht=111111&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=,&yr=,&pho=0&pets=0&parking=0&laundry=0&pnd=0&red=0&zso=0&att=renovated&days=any&ds=all&pmf=0&pf=0&zoom=6&rect=-78206177,38698372,-71240845,41586688&p=1&sort=days&search=maplist&disp=1&rid=40&rt=2&listright=true&isMapSearch=true&zoom=6',
        # 'http://www.zillow.com/search/GetResults.htm?spt=homes&status=100000&lt=010000&ht=111111&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=,&yr=,&pho=0&pets=0&parking=0&laundry=0&pnd=0&red=0&zso=0&att=renovated&days=any&ds=all&pmf=0&pf=0&zoom=4&rect=-127463379,28478348,-84572754,39588757&p=1&sort=days&search=maplist&disp=1&rid=41&rt=2&listright=true&isMapSearch=true&zoom=4',
        # 'http://www.zillow.com/search/GetResults.htm?spt=homes&status=100000&lt=010000&ht=111111&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=,&yr=,&pho=0&pets=0&parking=0&laundry=0&pnd=0&red=0&zso=0&att=renovated&days=any&ds=all&pmf=0&pf=0&zoom=6&rect=-80084839,38852542,-69362183,41438608&p=1&sort=days&search=maplist&disp=1&rid=40&rt=2&listright=true&isMapSearch=true&zoom=6',
        # 'http://www.zillow.com/search/GetResults.htm?spt=homes&status=100000&lt=010000&ht=111111&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=,&yr=,&pho=0&pets=0&parking=0&laundry=0&pnd=0&red=0&zso=0&att=renovated&days=any&ds=all&pmf=0&pf=0&zoom=5&rect=-118267823,40505446,-96822510,45452424&p=1&sort=days&search=maplist&disp=1&rid=62&rt=2&listright=true&isMapSearch=true&zoom=5',
        # # 'http://www.zillow.com/search/GetResults.htm?spt=homes&status=100000&lt=010000&ht=111111&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=,&yr=,&pho=0&pets=0&parking=0&laundry=0&pnd=0&red=0&zso=0&att=renovated&days=any&ds=all&pmf=0&pf=0&zoom=5&rect=-90911865,36244273,-69466553,41508577&p=1&sort=days&search=maplist&disp=1&rid=61&rt=2&listright=true&isMapSearch=true&zoom=5',
    )

    base_url = 'http://www.zillow.com'

    def parse(self, response):        
        print "here man"
        jsonresponse = simplejson.loads(response.body_as_unicode())
        # print jsonresponse
##        print response.body
##        jsonresponse = simplejson.loads(r'%s' % response.body)
        pages = jsonresponse["list"]["pagination"]
        total_count = jsonresponse["list"]["binCounts"]["totalResultCount"]
        print total_count

        pages_html = fromstring(pages)
        pages = pages_html.xpath('//li/a/@href')
        print len(pages)
        page_url = pages[0]
        print page_url

        for page_no in range(1,int(math.ceil(total_count/25.0))+1):        
            url = re.sub('\d{1}_p','%d_p'%page_no,page_url)
            print url            
            yield Request(self.base_url+url,self.get_links,dont_filter=True)
    
    def get_links(self, response):
        print "here in get links"
        hxs = Selector(response)
        property_urls = hxs.xpath('//a[@class="hdp-link routable"]/@href').extract()

        fp = webdriver.FirefoxProfile()
        fp.set_preference("network.cookie.cookieBehavior", 2)
        driver = webdriver.Firefox(firefox_profile=fp)

        # driver = webdriver.PhantomJS()
        # driver.set_window_size(1024, 768)
        for property_url in property_urls:
            property_full_url = self.base_url+property_url
            driver.get(self.base_url+property_url)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #TO scroll to bottom of page
            # pause = 2
            # lastHeight = driver.execute_script("return document.body.scrollHeight")
            # while True:
            #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #     time.sleep(pause)
            #     newHeight = driver.execute_script("return document.body.scrollHeight")
            #     print "scrolling down"
            #     if newHeight == lastHeight:
            #         print "broken"
            #         break
            #     lastHeight = newHeight

            time.sleep(1)
            html = driver.page_source
            # driver.close()
            driver.quit()
            hxs = fromstring(html)
            price_history_headers = hxs.xpath('//div[@id="hdp-price-history"]/section[@class="zsg-content-section null"][1]/table/thead/tr/th/text()')
            print price_history_headers
            price_history_rows = hxs.xpath('//div[@id="hdp-price-history"]/section[@class="zsg-content-section null"][1]/table/tbody/tr')
            print price_history_rows
            for price_history_row in price_history_rows:
                price_row_values = price_history_row.xpath('./td/text()')
                price_dict = dict(zip(price_history_headers,price_row_values))
                item = ZillowItem(**price_dict)
                item['propertyUrl'] = property_full_url

            # driver.close()
                phone = hxs.xpath('//span[contains(text(),"Property Owner")]/following-sibling::span[@class="snl phone"]/text()')
                print phone
                if phone:
                    item['ownerPhone'] = phone[-1]
                    print phone

                price = hxs.xpath('normalize-space(//div[@class="main-row  home-summary-row"]/span/text())')
                if price:
                    item['price'] = price

                # zestimate = hxs.xpath('//span[conatins(text(),"Zestimate")]/following-sibling::span[1]/text()').extract()
                zestimate = hxs.xpath('normalize-space(//div[@class="  home-summary-row"]/span[2]/text())')
                if zestimate:
                    item['zestimate'] = zestimate

                city_state_zip = hxs.xpath('//span[@class="zsg-h2 addr_city"]/text()')
                if city_state_zip:
                    print city_state_zip
                    city_state_zip = city_state_zip[0].split(',')
                    city = city_state_zip[0]
                    state_zip = city_state_zip[1].strip().split()
                    if state_zip:
                        print state_zip
                        state = state_zip[0]
                        zipcode = state_zip[1]
                        item['state'] = state
                        item['zipcode'] = zipcode

                    item['city'] = city

                street = hxs.xpath('//header[@class="zsg-content-header addr"]/h1/text()')
                if street:
                    item['street'] = street[0].rstrip(', ')


                beds_baths_sqfts = hxs.xpath('//span[@class="addr_bbs"]/text()')
                if len(beds_baths_sqfts) == 3:
                    item['beds'], item['baths'], item['sqfts'] = beds_baths_sqfts

                # price_history = hxs.xpath('//h2[contains(text(),"Price History")]/following-sibling::table[1]')
                # ptheaders = price_history.xpath('./thead/tr/th/text()')
                # ptrows = price_history.xpath('./tbody/tr')
                # for ptrow in ptrows:
                #     item['priceHistory'] = str(dict(zip(ptheaders,ptrow)))
                #     print "in loop"
                print item
                yield item

            # driver.close()
        # print price_history
        # elif len(beds_baths_sqfts) == 2:
        #     item

        # print item
        # yield  item




# http://www.zillow.com/AjaxRender.htm?encparams=6~6852217982799354020~-51qgQS0HHZy1fzb7hZAGvh9W5VuPQjk72UPSS_60hxIbZz3st3Dkrk0QMVgSFxzZiJ49ZpgBQzipLxHIS9jgsmkUe3o5ermD_VffpsoyIzOkUQ8bsOKjLImOMTb0gpeCBJ4ku-A0mBJm2xYHOFCtMKKKeFUw-5BJhPoqEloxfcgj_B7DqWFKApuSiO4fn6q12zooY-_VXv5Z7p9fnmFcC7KC_lKXxaelhU_zQwl235cMfQZbVO7AttSH08L5fPp40Id5V0IIJeRD4yWNI_V4YOb11GzoXTPwT288MBa4uT-stTsuO6d5YGeCUVfq5WYgClXjTgSN7Ws4HZtrH8_uA==&rwebid=9252491&rhost=1
# http://www.zillow.com/AjaxRender.htm?encparams=1~3401111969148978219~BTgU4MMW41dcqXKS9bU3Cj41w3WM_R_rWYHwNbgLH3zt7Sq_zDsNICxsqPs_AKAAK56fgsua9f6dd-TfTX_fHDh4ft_cnl1ZjbG5No0JYCLCAv7np_5gfHIMbXX6e17uANt5g_Qv3_EeRdampsBwvt59UWgSk6GqSLir3Dj43FrJ0NrUeE-bRp3zg25mbHue59OIb5UXcmAYyRVjomy2NUR2oatIzq7hKfbxxZs_sG46E-J9b2xr9jNfjYkSoqPCJHrhilcaMntXBMmto_hf4cxYvCbnc35aaUHFSq2JHxo=&rwebid=9252491&rhost=1
#
# http://www.zillow.com/AjaxRender.htm?encparams=9~2127873215617636926~OcNbRMgpqwRnyShX0-CTitxjhINGcnfmP5A1bK7cvHGDoXCTY4sxUjmfKSpl3nTCB3lkPAvwLC5PJlbY00nGkZmxzmyTyCYMDSLTLjXBzE71ZOIiTZl50nsGoaYg11bCoGaAAbj3MxatRZpRyLFMLAzAYgYspG36UVCSDFwZiSwedh0TrAOspYr7XoQXET8r&rwebid=9252491&rhost=1
#
# url:"/AjaxRender.htm?encparams=9~2127873215617636926~OcNbRMgpqwRnyShX0-CTitxjhINGcnfmP5A1bK7cvHGDoXCTY4sxUjmfKSpl3nTCB3lkPAvwLC5PJlbY00nGkZmxzmyTyCYMDSLTLjXBzE71ZOIiTZl50nsGoaYg11bCoGaAAbj3MxatRZpRyLFMLAzAYgYspG36UVCSDFwZiSwedh0TrAOspYr7XoQXET8r&rwebid=9252491&rhost=1",
# divId:"z-digs-upsell"}],id:"z-digs-upsell"},customEvent:"digsUpsell:renderUpsell",name:"z-digs-upsell",global:false,jsModule:"zillow-async-block",phaseType:"scroll",requires:["zillow-async-block"],initializer:"_create"});j.\
# {ajaxURL:"/AjaxRender.htm?encparams=8~5403813807930320319~u-b1GvovxmTVlQjOnhTuUFNojJgtsrbemkYpGZ47jkUQSnL7cyIewsu7m8osuSwHSLsiUDjeEiIV16V-e-5SF57leo8nujMUyCdX-aXWR7OrBbtwzqf1kt_kQIdXOqDh0jn1dR0yKmeOthVGTsQwEPxs0PuRNps3EWvMYCGzRyWGGeIEeQ_BzNglVVJ_cirvpk8QPj63ZIN5Gu6ZFjSA5A==&rwebid=9252491&rhost=1",jsModule:"z-scroll-event-tracker",phaseType:"scroll",divId:"fios-scroll-tracker",notificationEvent:"deferred:verizonFiosAd"});var g=k.one("#hdp-content");if(g){g.plug(k.Z.Plugin.HDPFactsSuite,{ignoreReorgClassName:""})}k.Z.UI.MoreLess.init({selector:".hdp-facts",toggleEvent:"hdp-facts"});new k.Z.HdpChartLoader({chartDivId:"paparazzi-chart",showForecast:true,metricMetaData:{"1":{st:"linear",tp:"tenYears",ft:"dollar",vt:"line"},"2":{st:"linear",tp:"tenYears",ft:"percent",vt:"line"},"3":{st:"linear",tp:"year",ft:"dollar",vt:"line"},"4":{st:"linear",tp:"fiveYears",ft:"dollar",vt:"stack"},"5":{st:"linear",tp:"fiveYears",ft:"dollar",vt:"line"},"6":{st:"log",tp:"month",ft:"raw",vt:"line"},"7":{st:"linear",tp:"year",ft:"dollar",vt:"line"},"8":{st:"linear",tp:"year",ft:"dollar",vt:"line"},"9":{st:"linear",tp:"year",ft:"dollar",vt:"line"},index:[1,2,3,4,5,6],"10":{st:"linear",tp:"year",ft:"dollar",vt:"line"}},state:{rt:"6,7,8",size:"standard",mt:1,zpid:39517578},paparazziEnabled:true,jsonRequestUrl:"http://ppz.zillowstatic.com:80/hdp_chart/render.json?v=2&h=54ycrjVM0t0h56gDfTIkczcLtDhGUa2CcW7MHZg9PR0%3D",epochs:{tenYears:[1134460800000,1449993600000],month:[1447401600000,1449993600000],year:[1418457600000,1449993600000],fiveYears:[1292227200000,1449993600000],day:[1449907200000,1449993600000]}});j.load({ajaxURL:"/AjaxRender.htm?encparams=7~2935873658814484216~RCLSifbs6ZTZ9giJCg-9Y3JGXrUBFnKlJ9mCdHokTpTIhg4hA2IK0Lh2jg55B-lVDI324Ysmla_SXEOriZU5n2xTfIFmuN5a7X3nIZywuExj20UicpqPFzT798wXHb5qFbWsoFE6jpBsHtxTOF1B9eq7M6mssv0g&rwebid=9252491&rhost=1",jsModule:"z-hdp-auto-quotes-trigger",phaseType:"scroll",divId:"hdp-auto-quotes-trigger"});j.load({ajaxURL:"/AjaxRender.htm?encparams=6~6852217982799354020~-51qgQS0HHZy1fzb7hZAGvh9W5VuPQjk72UPSS_60hxIbZz3st3Dkrk0QMVgSFxzZiJ49ZpgBQzipLxHIS9jgsmkUe3o5ermD_VffpsoyIzOkUQ8bsOKjLImOMTb0gpeCBJ4ku-A0mBJm2xYHOFCtMKKKeFUw-5BJhPoqEloxfcgj_B7DqWFKApuSiO4fn6q12zooY-_VXv5Z7p9fnmFcC7KC_lKXxaelhU_zQwl235cMfQZbVO7AttSH08L5fPp40Id5V0IIJeRD4yWNI_V4YOb11GzoXTPwT288MBa4uT-stTsuO6d5YGeCUVfq5WYgClXjTgSN7Ws4HZtrH8_uA==&rwebid=9252491&rhost=1",jsModule:"z-hdp-price-history",phaseType:"scroll",divId:"hdp-price-history"});j.load({ajaxURL:"/AjaxRender.htm?encparams=1~3401111969148978219~BTgU4MMW41dcqXKS9bU3Cj41w3WM_R_rWYHwNbgLH3zt7Sq_zDsNICxsqPs_AKAAK56fgsua9f6dd-TfTX_fHDh4ft_cnl1ZjbG5No0JYCLCAv7np_5gfHIMbXX6e17uANt5g_Qv3_EeRdampsBwvt59UWgSk6GqSLir3Dj43FrJ0NrUeE-bRp3zg25mbHue59OIb5UXcmAYyRVjomy2NUR2oatIzq7hKfbxxZs_sG46E-J9b2xr9jNfjYkSoqPCJHrhilcaMntXBMmto_hf4cxYvCbnc35aaUHFSq2JHxo=&rwebid=9252491&rhost=1",jsModule:"z-expando-table",phaseType:"scroll",divId:"hdp-tax-history"});j.load({ajaxURL:"/AjaxRender.htm?encodedRequestAdTargets=eyJhYW1nbnJjMSI6IjMwMSBFYXN0IEF2ZSIsImJkIjoiNCIsImNpdHkiOiJCYXlfSGVhZCIsImZzYmlkIjoiODU4OCIsImxpc3R0cCI6ImJ1eV9hZ2VudCIsImxvdCI6IjMiLCJtbGIiOiJwcjEwIiwibW92ZXIiOiJGb3JTYWxlIiwicGlkIjoiMzk1MTc1NzgiLCJwcmFuZ2UiOiI0bS00Xzk5OW0iLCJwcmljZSI6IjQ5MDAwMDAiLCJwcmljZV9iYW5kIjoiejNtIiwicHJvcHRwIjoic2ZoIiwicmVzaWRlbmNlVHlwZSI6IjkiLCJzcWZ0IjoiMjQ5NCIsInNxZnRyYW5nZSI6IjIwMDAtMjQ5OSIsInN0YXRlIjoiTkoiLCJ5cmJsdCI6IjE5NjAtMTk2OSIsInpfbGlzdGluZ19pbWFnZV91cmwiOiJodHRwOi8vcGhvdG9zMS56aWxsb3dzdGF0aWMuY29tL3BfZC9JU3hqNTlwOHVoMTVocjEwMDAwMDAwMDAuanBnIiwiemVzdGltYXRlIjoiNDY2MDUzOCIsInpndWlkaCI6Ii01OTkzMjgyMTUxMDYzNjM4MjgwIiwiemlwZXh0ZW5zaW9uIjoiNDcwNSIsInp1c3IiOiJ0cnVlIn0&encparams=8~6992023025006773908~tQYbWZJgAYVfZrjlmDro7u2f2yhZol-0yaVDYAJ_MtcGu5Zsj0iWG4ahGm50qZUz9KlxoDAeeUVpbWJg3xt3JIYjfKdEPwq9YqQuBEEMsIwgx030uF1y66Dd7MaZoMi6rLoNa3Kjf8WiKNKkl80nu6qr3dNRoMtngprdMzpX9cOKb8nvAUN3h_oBi0VpsHz3lZop2grck0I5jJ8fd7p6VCJdhfzvkKPTNGGpXjRlRrMp2eDfLkn9bJgRX5fRbHDqQcDQf0yC4QaBmBQGKm4kGfF0OGbZt3Q1gIIywX_AtWciRXgUT2qdH4j283dWFiR4y8CKugF2VDgwauy1Ua2TRg==&rwebid=9252491&rhost=1",jsModule:"z-hdp-async-mortgage-module",phaseType:"scroll",divId:"hdp-mortgage-module"});new k.Z.HdpOtherCosts();j.load({ajaxURL:"/AjaxRender.htm?encparams=2~4506352298740034075~I2ixIVCoW3yr6yNUUJrul5akgLBB3nBnlr6fSHBj9fxgvEFlsDAmOmKmI_Z7dw-TO010VJVVmFLGw1AnpdtDPgaKTA-tomAgcLk9-tht7rMfE95krs5xBU232_OY2Bp06YxS3JuaC6w0hksVcgEgqV7iOFnObKXC0S7TqprCBAh2oHyAEtDxJI9C6yFfOBeQlYlAry1dB4VfZ42babCgpg==&rwebid=9252491&rhost=1",jsModule:"z-scroll-event-tracker",phaseType:"scroll",divId:"other-costs-scroll-tracker",notificationEvent:"deferred:otherCostsIframe"});k.one("#walkscore-target").delegate("click",function(l){k.Z.Analytics.trackEvent({category:"Homes",action:l.target.getAttribute("data-za-action")})},".zsg-tooltip-launch");j.load({zoomLevel:17,mapInfo:{isPlan:false,subdivisionId:"",communityName:" ",premierCommunity:false},boundingBox:"#neighborhood-map",latLong:{latitude:40.073555,longitude:-74.041439},zpid:"39517578",googleEnabled:true,jsModule:"zillow-hdp-map-loader",phaseType:"scroll"});var h=new k.Z.GenericCarousel({viewableItems:1,viewableItemsAtWidth:{400:2,750:3},singleItemScroll:false,itemSpacing:5,btnWidth:25,scrollDuration:0.3,lazyLoadImages:true,lazyLoadImageAttribute:"data-src",container:".nearby-homes-carousel"});h.on("carousel:next",function(l){k.Z.track({category:"Homes",action:"Nearby homes next"})});h.on("carousel:prev",function(l){k.Z.track({category:"Homes",action:"Nearby homes previous"})});k.on("CollapsibleModule:expandSection",function(l){if(l.moduleName==="neighborhood"){h.fire("carousel:resize")}});j.load({ajaxURL:"/AjaxRender.htm?encparams=6~3842084996240117420~nDHavP_wQMtBAtnoOwtv9K5OTowASg-2DCycWfdMQaNQuT4JZYMOqnSekTl5rj89TXYdulUvYNxdRk2juzOICfBInqIDGUmwQ1_dAw6KY4XHSAeo5S-Pa9DRX6nxmb88KVi3tgYGEos5iBxGUGv595SQt0cfa6bD6AWA291cYOKsM3cgaRjyNo5zeZBHXZFh-7LvVzQJC1ro…

# http://www.zillow.com/search/GetResults.htm?spt=homes&status=100000&lt=111101&ht=111111&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=,&yr=,&pho=0&pets=0&parking=0&laundry=0&pnd=0&red=0&zso=0&att=renovated&days=any&ds=all&pmf=0&pf=0&zoom=6&rect=-78206177,38698372,-71240845,41586688&p=1&sort=days&search=maplist&disp=1&rid=40&rt=2&listright=true&isMapSearch=true&zoom=6
# http://www.zillow.com/search/GetResults.htm?spt=homes&status=100000&lt=010000&ht=111111&pr=,&mp=,&bd=0%2C&ba=0%2C&sf=,&lot=,&yr=,&pho=0&pets=0&parking=0&laundry=0&pnd=0&red=0&zso=0&att=renovated&days=any&ds=all&pmf=0&pf=0&zoom=5&rect=-118267823,40505446,-96822510,45452424&p=1&sort=days&search=maplist&disp=1&rid=62&rt=2&listright=true&isMapSearch=true&zoom=5