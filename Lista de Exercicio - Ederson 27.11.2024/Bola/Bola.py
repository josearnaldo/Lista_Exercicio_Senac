class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    def troca_cor(self, cor):
        self.cor = cor
    def mostrar_cor(self):
        print('A cor da bola é: ', self.cor)
        