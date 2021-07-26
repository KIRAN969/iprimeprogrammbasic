class Employee:
    name="raju"
    def printName(self):
        print(self.name)
Employee.printName=classmethod(Employee.printName)
Employee.printName()
