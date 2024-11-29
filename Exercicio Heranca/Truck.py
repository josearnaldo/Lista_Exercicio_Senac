from Vehicle import Vehicle
class Truck(Vehicle) :
    def __init__(self, brand, model):
        super().__init__(brand,model)
    def Type_fuel(self):
        return 'Diesel'
    def Capacity_Passenger(self):
        return 2
    