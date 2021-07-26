class Students:
    def __init__(self,name,rollno,adminno):
        self.myname=name
        self.myrollno=rollno
        self.myadminno=adminno
obj=[]
obj.append(Students("kiran",101,51001))
obj.append(Students("charan",102,51002))
obj.append(Students("kumar",103,51003))
print(obj[0].myname)
print(obj[1].myrollno)