class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def informacao(self):
        print(self.nome)
        print(self.idade)