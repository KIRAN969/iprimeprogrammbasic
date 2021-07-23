n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
n3=int(input("enter a number:"))
list1=[n1,n2,n3]
def sqr(a):
    return a**2
print(tuple(map(sqr,list1)))