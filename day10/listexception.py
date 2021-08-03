l=[12,56,123,45]
try:
    #print(l[2])
    print(a[5])
except (IndexError,NameError):
    print("enter correct index value")
else:
    print("execution completed successfully")
finally:
    print("ok done completed")