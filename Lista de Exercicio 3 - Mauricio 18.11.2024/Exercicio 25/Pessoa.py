class Pessoa:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura
    def calcular_imc(self):
        print(f'Peso: {self.peso}')
        print(f'Altura:{self.altura}')
        print(f'IMC: {(self.peso/(self.altura**2)):.2f}')