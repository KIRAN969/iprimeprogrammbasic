import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase=client['productDb']
collection_name=mydatabase['products']

productlist=[]
class Products:
    def addProducts(self,productcode,pname,distributername,manu_year,wholesaleprice,retailprice,productdescription,manu_mobnum):
        dict{"productcode":productcode,"pname":pname,"distributername":distributername,"manu_year":manu_year,"wholesaleprice":wholesaleprice,"retailprice":retailprice,"productdescription":productdescription,"manu_mobnum":manu_mobnum}
        productlist.append(dict)
obj=Products()

while(1):
    print("1.add product")
    print("2.view product")
    print("3.search product")
    print("4.exit")
    choice==int(input("enter yourchoice:"))

    if choice==1:
        productcode=input("enter the product code:")
        pname=input("enter the product name:")
        distributername=input("enter the distributer name:")
        manu_year=input("enter the manufacturing year:")
        wholesaleprice=input("enter the wholesale price:")
        retailprice=input("enter the retail price:")
        productdescription=input("enter the product description:")
        manu_mobnum=input("enter the manufacture mobile number:")
        obj.addProducts(productcode,pname,distributername,manu_year,wholesaleprice,retailprice,productdescription,manu_mobnum))
        result=collection_name.insert_many(productlist)
        print(result.inserted_ids)

    if choice==2:
        result=collection_name.find()
        for i in result:
            studentlist.append(i)
        print(i)

    if choice==3:
        n=input("enter product code")
        k=productlist.find({"productcode":n})
        for i in k:
            print(i)
        
    if choice==4:
        break
