class department:
    def __init__(self,dept):
        self.dept=dept
    def addStudent(self):
        self.sname=input("enter your name:")
        self.sroll=int(input("enter your rollno:"))
        self.sadmin=int(input("enter your adminno:"))
        self.scollege=input("enter your college:")
        self.saddr=input("enter your address:")
        self.smob=int(input("enter your mobileno:"))
        print("department is:",self.dept)
        print("name:",self.sname)
        print("rollno:",self.sroll)
        print("adminno:",self.sadmin)
        print("college:",self.scollege)
        print("address:",self.saddr)
        print("mobileno:",self.smob)
s1=department("cse")
s1.addStudent()
print("\n")
s2=department("ECE")
s2.addStudent()

