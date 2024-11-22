class Pessoa:
    def __init__(self, altura):
        self.altura = float(altura)
    def verificar_altura(self):
        if(self.altura>1.75):
            return print('Pessoa é maior que 1.75')
        else:
            return print('Pessoa é menor que 1.75')