class RBI:
    def interestRate(self):
        print("10%")
class SBI(RBI):
    def interestRate(self):
        print("8.5%")
class ICICI(RBI):
    def interestRate(self):
        print("9%")
class AXIS(RBI):
    def interestRate(self):
        print("6%")
obrbi=RBI()
obrbi.interestRate()
obsbi=SBI()
obsbi.interestRate()
obicici=ICICI()
obicici.interestRate()
obaxis=AXIS()
obaxis.interestRate()