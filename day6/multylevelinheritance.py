class India:
    def alotNumber(self,number):
        print(number)
class CarManufacturer(India):
    def makeACar(self,brand,color,price):
        print(brand,color,price)
class Seller(CarManufacturer):
    def customerOrder(self,name,mobno):
        print(name,mobno)
objseller=Seller()
objseller.customerOrder("kiran",6300902344)
objseller.makeACar("bmw","blue",150000)
objseller.alotNumber("AP12K1215")

