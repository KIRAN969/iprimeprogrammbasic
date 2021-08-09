import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase=client['students']
collection_name=mydatabase['students']
getname=input("enter a name:")
getroll=input("enter a rollno:")
getadm=input("enter a admno:")
getcollege=input("enter a college:")

data={"name":getname,"rollno":getroll,"admno":getadm,"college":getcollege}
#print(data)
result=collection_name.insert_one(data)
print(result.inserted_id)