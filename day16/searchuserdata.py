import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase=client['students']
collection_name=mydatabase['students']
result=collection_name.update_one({"rollno":"11"},{"$set":{"name":"kiran"}})
#print(result.updated_one)
# studentlist=[]
# for i in result:
#     studentlist.append(i)
#     print(studentlist)