
class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
    
    def description(self):
        return f"{self.make} {self.model} {self.year}, weight: {self.weight} kg"

    def total_weight(vehicle): #list of vehicle objects
        return sum(vehicle.weight for vehicle in vehicles)

class Car(Vehicle):
    def __init__(self , make,model, year ,weight, num_door):
        super().__init__(make, model, year, weight)
        self.num_door = num_door

    def description(self):
        return super().description() + f", {self.num_door} doors"

class Truck(Vehicle):
    def __init__(self, make, model, year, weight, payload_capacity):
        super().__init__(make, model, year, weight)
        self.payload_capacity = payload_capacity

    def description(self):
        return super().description() + f", payload capacity: {self.payload_capacity} kg"

#creating vehicle objects
car1 = Car("Toyota", "Camry", 2020, 1500.0, 4)
truck1 = Truck("Ford", "F-150", 2022, 2500.0, 800.0)


#create a list of vehicle objects
vehicles = [car1, truck1]


for vehicle in vehicles:
    print(vehicle.description())

print(f"Total weight of all vehicles: {Vehicle.total_weight(vehicles)} kg")





    
    



