class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def myfunc(self):
        print("I drive a " + self.make + " " + self.model + ".")

class Vehicle(Car):
    def __init__(self, make, model):
        super().__init__(make, model)

car1 = Car("Chevy", "Impala")
car2 = Car("Ford", "F150")

veh1 = Vehicle("Toyota", "Camry")

car1.myfunc()
car2.myfunc()
veh1.myfunc()