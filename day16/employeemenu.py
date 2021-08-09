import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase=client['employeeDb']
collection_name=mydatabase['employees']
employee_list=[]
employeefetchlist=[]
class Employees:
    def AddEmployees(self,name,address,mobnum,designation,salary,company):
        dict={"name":name,"address":address,"mobnum":mobnum,"designation":designation,"salary":salary,"company":company}
        employee_list.append(dict)
obj=Employees()
while(1):
    print("1.add employee:")
    print("2.view employee:")
    print("3.search employee:")
    print("4.exit:")
    option=int(input("enter your choice:"))
    if option==1:
        name=input("enter the name:")
        address=input("enter the address:")
        mobnum=input("enter the mobile number:")
        designation=input("enter the designation:")
        salary=input("enter the salary:")
        company=input("enter the company:")
        obj.AddEmployees(name,address,mobnum,designation,salary,company)
        result=collection_name.insert_many(employee_list)
        print(result.inserted_ids)

    if option==2:
        result=collection_name.find()
        for i in result:
            employeefetchlist.append(i)
        print(i)

    if option==3:
        result=collection_name.find({"name":kiran})

    if option==4:
        break
        
