# import threading,time
# def printNumbers():
#     for i in range(1,4):
#         time.sleep(3)
#         print(i)
# def printHello():
#     for i in range(1,5):
#         time.sleep(2)
#         print("hello")
# t1=threading.Thread(target=printNumbers)
# t2=threading.Thread(target=printHello)
# t2.start()
# t1.start()
# t1.join()
# t2.join()
# print("..........")


import threading,time
def findsquare(getlist):
    for i in getlist:
        time.sleep(3)
        print(i*i)
def findcube(getlist):
    for i in getlist:
        time.sleep(2)
        print(i*i*i)
mylist=[2,3,5,6]
t1=threading.Thread(target=findsquare,args=(mylist,))
t2=threading.Thread(target=findcube,args=(mylist,))
t1.start()
t2.start()
t1.join()
t2.join()
print("..........")

