# import multiprocessing,time
# def findsquare(getlist):
#     for i in getlist:
#         time.sleep(3)
#         print(i*i)
# def findcube(getlist):
#     for i in getlist:
#         time.sleep(2)
#         print(i*i*i)

# if(__name__=='__main__'):
#     mylist=[2,3,5,6]
#     p1=multiprocessing.Process(target=findsquare,args=(mylist,))
#     p2=multiprocessing.Process(target=findcube,args=(mylist,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print("..........")


import multiprocessing,time
def findeven(getlist):
    for i in getlist:
        time.sleep(3)
        if i%2==0:
            print("even> ",i)
def findodd(getlist):
    for i in getlist:
        time.sleep(2)
        if i%2!=0:
            print("odd> ",i)

if(__name__=='__main__'):
    mylist=[2,3,5,6]
    p1=multiprocessing.Process(target=findeven,args=(mylist,))
    p2=multiprocessing.Process(target=findodd,args=(mylist,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("..........")