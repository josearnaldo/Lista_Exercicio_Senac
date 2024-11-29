from Vehicle import Vehicle
class Motorcycle(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand,model)
    def Type_fuel(self):
        return 'Gasoline'
    def Capacity_Passenger(self):
        return 2


