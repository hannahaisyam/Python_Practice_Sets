#1 Define a property that must have the same value for every class instance (object)
class Vehicle:
    color = "Red"

    def __init__(self, name, max_speed, mileage):
            self.name = name
            self.max_speed = max_speed
            self.mileage = mileage
    
class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass


#School_bus = Bus("School Volvo", 180, 12)
#print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

#car = Car("Audi Q5", 240, 18)
#print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)


#2 Class Inheritance 

class Carnival:
    
    def __init__(self, name,month, number):
        self.name = name
        self.month = month
        self.number = number

    def fare(self):
        return self.number * 7
    
    def desc_info(self):
        print(f"The {self.name} Carnival is held during the whole {self.month}. Each ticket price* is {self.fare()} ")

    
class Ticket(Carnival):
    def total(self):
        total_fare = super().fare()
        total_fare += total_fare *0.1
        return total_fare
       
    
Carnival_tix = Ticket("Corn", "February" , 1)
Carnival_tix.desc_info()
print("Total ticket fare is:", Carnival_tix.total())

#3 Check type of an object and check if School_bus is instance 

print(type(Carnival))
print(isinstance(Carnival_tix, Carnival))