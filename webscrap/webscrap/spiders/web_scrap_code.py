import scrapy
from scrapy.http import  Request
from ..items import  WebscrapItem
class webscrap(scrapy.Spider):
    name='flipcart'
    next_page=2
    #men topwear first page link
    #start_urls=['https://www.flipkart.com/clothing-and-accessories/topwear/pr?sid=clo%2Cash&otracker=categorytree&p%5B%5D=facets.ideal_for%255B%255D%3DMen&page=1']

    #womens footwear  first page link
    start_urls=['https://www.flipkart.com/womens-footwear/pr?sid=osp%2Ciko&otracker=nmenu_sub_Women_0_Footwear&page=1']
    url=start_urls[0]
    def parse(self,response):
        collection=WebscrapItem()
        #name of product
        name=response.css(".IRpwTa::text").extract()
        #brand of the product
        brand=response.css("._2WkVRV::text").extract()
        #original_price price of the prodct
        original_price=response.css("._3I9_wc::text").extract()
        #sale price price of the product
        sale_price=response.css("._30jeq3::text").extract()
        #image url of the  product
        image_url=response.css("._2r_T1I::attr(src)").extract()
        #product paage url
        product_page_url=webscrap.url
        #product category
        product_category=response.xpath('//a[@class="_1jJQdf _2Mji8F"]/text()').extract()
        #create new list for remove ',' and '₹' in original_price and sale_price
        data_original_price=[]
        data_sale_price=[]
        for i in original_price:
            if i!='₹':
                i=i.replace(',','')
                data_original_price.append(float(i))
        for j in sale_price:
            j=j.replace('₹','')
            j=j.replace(',','')
            data_sale_price.append(float(j))
        #store all products information in collection
        collection["name"]=name
        collection["brand"]=brand
        collection["original_price"]=data_original_price
        collection["sale_price"]=data_sale_price
        collection["image_url"]=image_url
        collection["product_page_url"]=product_page_url
        collection["product_category"]=product_category
        yield collection

        #dynamic link for men topwear product
        #next_page='https://www.flipkart.com/clothing-and-accessories/topwear/pr?sid=clo%2Cash&otracker=categorytree&p%5B%5D=facets.ideal_for%255B%255D%3DMen&page='+str(webscrap.next_page)


        #dynamic link for womens footwear product
        next_page='https://www.flipkart.com/womens-footwear/pr?sid=osp%2Ciko&otracker=nmenu_sub_Women_0_Footwear&page='+str(webscrap.next_page)
        if webscrap.next_page<26:
            webscrap.next_page+=1
            webscrap.url=next_page
            #this is for go next paage for product
            yield response.follow(next_page,callback=self.parse)


































































































































































































































































































































                    # elif webscrap.next_page>1:
                    #     webscrap.next_page=2
                    #     webscrap.start_urls[0]='https://www.flipkart.com/womens-footwear/pr?sid=osp%2Ciko&otracker=nmenu_sub_Women_0_Footwear&page=1'
                    #     webscrap.url=webscrap.start_urls[0]
                    #     name=response.css(".IRpwTa::text").extract()
                    #     brand=response.css("._2WkVRV::text").extract()
                    #     original_price=response.css("._3I9_wc::text").extract()
                    #     sale_price=response.css("._30jeq3::text").extract()
                    #     image_url=response.css("._2r_T1I::attr(src)").extract()
                    #     product_page_url=webscrap.url
                    #     product_category=response.xpath('//a[@class="_1jJQdf _2Mji8F"]/text()').extract()

                    #     #create new list for remove ',' and '₹' in original_price and sale_price
                    #     data_original_price=[]
                    #     data_sale_price=[]
                    #     #this loop use for remove '₹' and ',' from original_price
                    #     for i in original_price:
                    #         if i!='₹':
                    #             i=i.replace(',','')
                    #             data_original_price.append(float(i))
                    #     #this loop use for remove ','  and '₹' from sale_price
                    #     for j in sale_price:
                    #         j=j.replace('₹','')
                    #         j=j.replace(',','')
                    #         data_sale_price.append(float(j))

                    #     collection["name"]=name
                    #     collection["brand"]=brand
                    #     collection["original_price"]=data_original_price
                    #     collection["sale_price"]=data_sale_price
                    #     collection["image_url"]=image_url
                    #     collection["product_page_url"]=product_page_url
                    #     collection["product_category"]=product_category
                    #     yield collection
                    #     next_page='https://www.flipkart.com/womens-footwear/pr?sid=osp%2Ciko&otracker=nmenu_sub_Women_0_Footwear&page='+str(webscrap.next_page)

                    #     if webscrap.next_page<26:

                    #         webscrap.next_page+=1
                    #         webscrap.url=next_page
                    #         print(webscrap.next_page)
                    #         yield response.follow(next_page,callback=self.parse)
