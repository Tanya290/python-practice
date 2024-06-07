#data abstraction:
#it hides unnecessary code details from the user
#also,when we don't want to give out sensitive parts of our code implementation and this is where data abstraction came
#in oython it can be achieved by creating abstract classes


#abstract base class
from abc import ABC, abstractSmethod
class car(ABC):
    def mileage(self):
        pass

class bmw(car):
    def mileage(self):
        print("the mileage is 30 kmph")

class volkswagen(car):
    def mileage(self):
        print("the mileage is 27 kmph")

class mercedes(car):
    def mileage(self):
        print("the mileage is 25 kmph")

class ford(car):
    def mileage(self):
        print("the mileage is 15 kmph")


#example
b=bmw()
b.mileage()

v=volkswagen()
v.mileage()

m=mercedes()
m.mileage()

f=ford()
f.mileage()
