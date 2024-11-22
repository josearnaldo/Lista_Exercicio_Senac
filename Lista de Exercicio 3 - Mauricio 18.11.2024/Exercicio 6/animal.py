class Animal:
    def __init__(self, animal, barulho):
        self.animal = animal
        self.barulho = barulho
    def som(self):
        return print('Animal: ',self.animal,'Som: ', self.barulho)