class Addition:
    def add(self,a,b):
        return a+b
class Subtraction:
    def sub(self,a,b):
        return a-b
class Multiplication:
    def mul(self,a,b):
        return a*b
class Calculator(Addition,Subtraction,Multiplication):
    pass
objcalc=Calculator()
# n1=int(input("enter a number:"))
# n2=int(input("enter a number:"))
# print(objcalc.add(n1,n2))
# print(objcalc.sub(n1,n2))
# print(objcalc.mul(n1,n2))
print(issubclass(Calculator,Addition))
print(issubclass(Addition,Multiplication))