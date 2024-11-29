class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def Envelhecer(self,anos):
        if self.idade<21:
            for i in range(self.idade, anos):
                self.altura= 0.5
            self.idade+= anos
            print(self.altura)
            print(self.lidade)
        else:
            self.idade+= anos
            print(self.idade)
            print(self.altura)
    def engordar(self, peso):
        self.peso = self.peso+peso
        print(self.peso)
    def emagrecer(self, peso):
        self.peso = self.peso - peso
        print(self.peso)
    def crescer(self):
        if(self.idade<21):
            self.altura+= 0.5
            self.idade+=1
            print(self.idade)
            print(self.altura)
        else:
            self.idade+=1
            print(self.idade)
            print(self.altura)