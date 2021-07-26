class department:
    def __init__(self,deptname):
        self.mydept=department
    def addStudent(self,sname,srollno,sadminno,saddress,scollege,smobileno):
        print(self.mydept)
name=input("enter name:")
rollno=int(input("enter rollno:"))
adminno=int(input("enter adminno:"))
address=input("enter address:")
college=input("enter college name:")
mobile=int(input("enter mobile no:"))
dept=department()