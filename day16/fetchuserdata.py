import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase=client['students']
collection_name=mydatabase['students']
result=collection_name.find({},{"_id":0})
for i in result:
    print(i)
# result=collection_name.find_one()
# print(result)