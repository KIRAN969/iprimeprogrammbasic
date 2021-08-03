# n1=int(input("enter a number:"))
# n2=int(input("enter a number:"))
try:
    n1=int(input("enter a number:"))
    n2=int(input("enter a number:"))
    div=n1/n2
    print(div)
except ZeroDivisionError:
    print("oops!something went wrong")
except ValueError:
    print("enter a value not letter")