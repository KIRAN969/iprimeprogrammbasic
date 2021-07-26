class Cars:
    def mineColor(self,color):
        self.color=color
        print(self.color)
class Toyoto(Cars):
    def topSpeed(self,speed):
        self.speed=speed
        print(self.speed)
objcars=Cars()
objtoyoto=Toyoto()
# objcars.mineColor("red")
# objcars.topSpeeb(100)
objtoyoto.mineColor("blue")
objtoyoto.topSpeed(200)