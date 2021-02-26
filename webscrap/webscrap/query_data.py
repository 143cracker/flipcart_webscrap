from pipelines import WebscrapPipeline
import pymongo


class query:
    database=WebscrapPipeline()
    db=database.conn["bansh"]
    #data base name

    def first_query(self):
        data=query.db.flipcart.find({})
        data1=[]
        for i in data:
            data1.append(len(i['brand']))


        #total product scrap
        print(sum(data1))
        #result=2000

    def second_query(self):
        data2=query.db.flipcart.find({})
        sale_price=[]
        original_price=[]
        count=0
        for i in data2:
            sale_price+=i['sale_price']
            original_price+=i['original_price']
        for x,y in zip(sale_price,original_price):
            if x<y:
                count+=1


        #this is discont product
        print(count)
        #result=1779

    def third_query(self):
        data3=query.db.flipcart.find({})
        sale_price=[]
        original_price=[]

        count=0
        for i in data3:
            if i['product_category'][0]=='Topwear':
                sale_price+=i['sale_price']
                original_price+=i['original_price']
        for x,y in zip(sale_price,original_price):
                if x<y:
                    count+=1



        #total Men's Topwear products don't have any discount on them
        print(count)
        #result=992




    def forth_query(self):
        data4=query.db.flipcart.find({})
        brand_count=0
        for i in data4:
            brand_count+=len(set(i['brand']))


        #total brand product
        print(brand_count)
        #result=1641

    def fifth_query(self):
        data5=query.db.flipcart.find({})
        sale_price=[]
        original_price=[]
        count=0
        for i in data5:
            if i['brand']:
                sale_price+=i['sale_price']
                original_price+=i['original_price']
        for x,y in zip(sale_price,original_price):
            if x>=y:
                count+=1


        #total count of discounted products for each brand?
        print(count)
        #result=175


    def six_query(self):
        data6=query.db.flipcart.find({})
        name=[]
        count=0
        for i in data6:
            name+=i['name']
        for i in name:
            if 'Shirt' in i:
                count+=1


        #total count products have shirt in their name
        print(count)
        #result=982

    def seven_query(self):
        data7=query.db.flipcart.find({})
        sale_price=[]
        original_price=[]
        count=0
        for i in data7:
            sale_price+=i['sale_price']
            original_price+=i['original_price']
        for x,y in zip(sale_price,original_price):
            if (y-x)>300:
                count+=1



        #total count products have offer price greater than 300?
        print(count)
        #result=1565



    def eight_query(self):
        data8=query.db.flipcart.find({})
        sale_price=[]
        original_price=[]
        count=0
        for i in data8:
            sale_price+=i['sale_price']
            original_price+=i['original_price']
        for x,y in zip(sale_price,original_price):
            if round(y*(3/10))>=x:
                count+=1


        #total count products have discount % greater than 30%?
        print(count)
        #reslt=744




    def nine_query(self):
        data8=query.db.flipcart.find({})
        sale_price=[]
        original_price=[]
        count=0
        for i in data8:
            if i['product_category'][0]=="Women's Footwear":
               sale_price+=i['sale_price']
               original_price+=i['original_price']
        for x,y in zip(sale_price,original_price):
            if round(y*(1/2))>=x:
                count+=1


        #total Women's footwear products have a 50% discount?
        print(count)
        #result=572
    # def ten_query(self):
    #     data10=self.db.flipcart()
    #     return data10


query_object=query()
query_object.first_query()
query_object.second_query()
query_object.third_query()
query_object.forth_query()
query_object.fifth_query()
query_object.six_query()
query_object.seven_query()
query_object.eight_query()
query_object.nine_query()
