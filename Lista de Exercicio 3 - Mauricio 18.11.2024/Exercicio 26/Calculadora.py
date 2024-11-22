class Calculadora:
    def __init__(self):
        self.lista = []
        self.registro =0
    def somar(self, x,y):
        
        self.registro +=1
        z = x+y
        print(z)
        self.lista.append(f'({self.registro}) {x} + {y} = {z}')
        x=0
        y=0

    def subtrair(self, x, y):
        self.registro +=1
        z = x-y
        print(z)
        self.lista.append(f'({self.registro}) {x} - {y} = {z}')
        x=0
        y=0
    def multiplicar(self, x,y):
        self.registro +=1
        z = x*y
        print(z)
        self.lista.append(f'({self.registro}) {x} * {y} = {z}')
        x=0
        y=0
    def dividir(self, x,y):
        if(y==0):
            self.registro+=1
            self.lista.append(f'({self.registro})NAN')
        else:
            self.registro +=1
            z = x/y
            print(z)
            self.lista.append(f'({self.registro}) {x} + {y} = {z}')
            x=0
            y=0
    def exibir_historico(self):
        for i in range(0, len(self.lista)):
            print(self.lista[i])
        