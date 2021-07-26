class Animal:
    def speak(self):
        print("animal speak")
class Cow(Animal):
    def eat(self):
        print("eat grass")
b=Cow()
b.eat()
