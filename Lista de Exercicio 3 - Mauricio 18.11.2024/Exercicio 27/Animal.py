class Animal:
    def __init__(self, nome, movimento):
        self.nome = nome
        self.movimento = movimento
    def mover(self):
        print(f'{self.nome},o movimento que faz é :{self.movimento}')
        