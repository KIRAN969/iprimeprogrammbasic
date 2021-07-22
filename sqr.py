n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
n3=int(input("enter a number:"))
list=[n1,n2,n3]
def sqr(a):
    return a**2
    print(list(map(sqr,list)))