# class A:
#     def sayHello(self):
#         print("hello")
# class B(A):
#     def sayHello(self):
#         print("hi")
# oba=A()
# obb=B()
# oba.sayHello()
# obb.sayHello()

def add(a,b,c=0):
    return a+b+c
print(add(2,3))
print(add(2,3,4))