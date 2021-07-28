class Addition:
    def add(self,a,b):
        return a+b
class Subtraction:
    def sub(self,a,b):
        retuen a-b
class Multiplication:
    def mul(self,a,b):
        return a*b
class Calculator(Addition,Subtraction,Multiplication):
    pass
objcalc=Calculator()
n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
print(onjcalc.add(n1,n2))
print(onjcalc.sub(n1,n2))
print(onjcalc.mul(n1,n2))