from Vehicle import Vehicle
from Car import Car
from Motorcycle import Motorcycle
from Truck import Truck


car = Car('Ford', 'mustang')
motorcycle = Motorcycle('Kawasaki', 'Ninja')
truck = Truck('Mercedes', 'Actros')

print(f' Model : {car.model}, Brand: {car.brand}, Fuel:{car.Type_fuel()}, Passenger:{car.Capacity_Passenger()}')
print(f' Model : {motorcycle.model}, Brand: {motorcycle.brand}, Fuel:{motorcycle.Type_fuel()}, Passenger :{motorcycle.Capacity_Passenger()}')
print(f' Model : {truck.model}, Brand: {truck.brand}, Fuel:{truck.Type_fuel()},Passenger: {truck.Capacity_Passenger()}')


