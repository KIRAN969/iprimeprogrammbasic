import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase=client['collegeDb']
collection_name=mydatabase['students1']
studentlist=[]

while(1):
    print("\n1.add student:")
    print("\n2.search student:")
    print("\n3.update student:")
    print("\n4.delete student:")
    print("\n5.view  student count of each branch:")
    print("\n6.exit :")
    
    ch=int(input("enter your choice:"))

    if ch==1:
        name=input("enter the name:")
        rollno=input("enter the rollno:")
        branch=input("enter the branch:")
        mydict={"name":name,"rollno":rollno,"branch":branch}
        studentlist.append(mydict)
        collection_name.insert_many(studentlist)
        studentlist.clear()

    if ch==2:
         name=input("enter the name:")
         result=collection_name.find({"name":name})
         for i in result:
             print(i)

    if ch==5:
        result=collection_name.aggregate([{"$group":{"_id":"$branch","count":{"$sum":1}}}])
        for i in result:
            print(i)