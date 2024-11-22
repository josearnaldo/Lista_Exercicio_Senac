class Carro:
    def __init__(self, marca, combustivel):
        self.marca= marca
        self.combustivel = combustivel
    def abastecer(self,abastecimento):
        self.combustivel = self.combustivel + abastecimento
    def exibir_nivel(self):
        print('Nivel do combustivel está em ', self.combustivel)