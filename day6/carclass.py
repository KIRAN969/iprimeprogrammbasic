class cars:
    colour="black"
    brand="BMW"

    def findMilage(self,lit,km):
        return km/lit

myCar=cars()
a1=input("enter colour:")
a2=input("enter brand:")
l=int(input("enter liters:"))
k=int(input("enter kilometers:"))
milage=myCar.findMilage(l,k)
myCar.colour=a1
myCar.brand=a2
print(myCar.colour)
print(myCar.brand)
print(milage)
