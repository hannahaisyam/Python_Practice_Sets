#1 Create a class with intance attribute

class Vehicale:
    def __init__(self, name, max_speed, mileage):

        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def seating_capacity(self,capacity):
        return f"The seating capacity of a {self.name} is {capacity} passangers"


model = Vehicale(245,75)
print(model.max_speed, model.mileage)


#2 Create a Student class w/o any variables or methods
class Name:
    pass

    
#3 Create a child class Bus that will inherit all variables and method of the House
class Bus(Vehicale):
    pass

bus = Bus("Ford", 80 , 25)
print(f"Vehicale name : {bus.name} , Speed : {bus.max_speed}, Mileage : {bus.mileage}")


#4 Class Inheritance 
class House:
    def __init__(self, name, color, type):
        self.name = name
        self.max_color = color
        self.type = type

    def people_capacity(self,capacity):
        return f"The guest capacity in a {self.type} is {capacity} people"

class People(House):
    def people_capacity(self, capacity =10):
        return super().people_capacity(capacity =10)
    

house = People("Mark", "Blue" , "Condo")
print(house.people_capacity())