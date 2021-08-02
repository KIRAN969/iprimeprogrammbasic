try:
    n1=int(input("enter a number:"))
    if n1<0:
        raise ValueError(n1)
    else:
        print(n1)
except ValueError:
    print("value is out of range.")