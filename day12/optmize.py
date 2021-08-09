import timeit
#print(timeit.timeit(stmt="a=10;b=5;c=a+b"))
# mycode='''A=10+5'''
# print(timeit.timeit(stmt=mycode))

# def printnumbers():
#     for n in range(1000):
#         pass

# def printwhile():
#     n=0
#     while(n<1000):
#         n=n+1
#         pass

mylist=[12,23,45,256,125,456,258,12,45,85,78,98,156,4521,32,569]
def f1():
    filter(12,mylist)
def f2():
    for i in mylist:
        if(i==12):
            pass

print(timeit.timeit(f1,number=10000000))
print(timeit.timeit(f2,number=10000000))
