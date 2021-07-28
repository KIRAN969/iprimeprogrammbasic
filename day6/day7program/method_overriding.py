class Car:
    def color(self):
        print("red")
class BMW(Car):
    def color(self):
        print("white")
objbmw=BMW()
objbmw.color()
objcar=Car()
objcar.color()