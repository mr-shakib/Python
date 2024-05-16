#POLYMORPHISM : method or function with same name but different signature

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self): #method with same name
        print(f'{self.brand} of model {self.model} is moving') #different signature

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self): #method with same name
        print(f'{self.brand} of model {self.model} is sailing')   #different signature

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self): #method with same name
        print(f'{self.brand} of model {self.model} is flying')   #different signature

car1 = Car("Audi", "A7")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", 747)


for x in (car1,boat1,plane1):
    x.move()