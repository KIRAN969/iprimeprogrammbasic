import functools
lis=[1,3,5,6,2]
print("sum is: ")
print(functools.reduce(lambda a,b:a+b,lis))
print("max element is: ")
print(functools.reduce(lambda a,b:a if a>b else b,lis))