import collections
n=int(input("length of list:"))
l1=[]
for i in range(n):
    names=input("enter the names:")
    l1.append(names)
print(l1)
x=collections.Counter(l1)
print(x)