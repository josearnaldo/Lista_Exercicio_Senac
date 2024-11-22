class Eletrodomestico():
    def __init__(self, nome, potencia):
        self.nome = nome
        self.potencia = potencia
    def ligar(self):
        print('Aparelho ligado')
    def desligar(self):
        print('Aparelho desligado')