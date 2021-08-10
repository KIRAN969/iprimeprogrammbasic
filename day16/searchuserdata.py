import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase=client['students']
collection_name=mydatabase['students']
result=collection_name.find({},{"_id":0,"name":0})
# print(result)
#print(result.updated_one)
studentlist=[]
for i in result:
    studentlist.append(i)
    print(studentlist)