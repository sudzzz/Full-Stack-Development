from json import JSONEncoder
import json
class Vehicle:
    def __init__(self,name,max_speed,milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage
    def seatCapacity(self,capacity):
        return f'The seating capacity of {self.name} is {capacity} persons'

class Car(Vehicle):
    def seatCapacity(self, capacity=50):
        return super().seatCapacity(capacity)
    def getFare(self,persons):
        fare = 100*persons
        if(persons >= 5):
            fare = fare*1.1
        return fare
    
def vehicleDecoder(obj):
    return Vehicle(obj['name'],obj['max_speed'],obj['milage'])

vehicleObj1 = json.loads('{"name":"Toyota,"max_speed":125,"milage":15}',object_hook=vehicleDecoder)

print(vehicleObj1.name, vehicleObj1.max_speed, vehicleObj1.mileage)

class VehicleEncoder(JSONEncoder):
    def default(self, o) :
        return o.__dict__

vehicle = Vehicle("Toyota",125,15)
vehicleJSON = json.dumps(vehicle,indent=4,cls=VehicleEncoder)
print(vehicleJSON)
    
hondaCar = Car("City",120,15)
# print(hondaCar.name,hondaCar.max_speed,hondaCar.milage)
# print(hondaCar.seatCapacity(7))
# print(hondaCar.getFare(5))