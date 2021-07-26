class calculator():
    def findCal(self,a,b):
        return a+b
    def findCal1(self,a,b):
        return a-b
    def findCal2(self,a,b):
        return a*b
    def findCal3(self,a,b):
        return a/b
    def findCal4(self,a,b):
        return a//b

myCal=calculator()
n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
add=myCal.findCal(n1,n2)
sub=myCal.findCal1(n1,n2)
mul=myCal.findCal2(n1,n2)
div=myCal.findCal3(n1,n2)
floordiv=myCal.findCal4(n1,n2)
print(add,sub,mul,div,floordiv)

    