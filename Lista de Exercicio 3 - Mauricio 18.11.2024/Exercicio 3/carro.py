class Carro:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano
    def informacoes(self):
        return print('Marca:',self.marca,' Ano:', self.ano)
        