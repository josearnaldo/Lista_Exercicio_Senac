class Retangulo:
    def __init__(self, LadoA, LadoB):
        self.LadoA = LadoA
        self.LadoB = LadoB
    def mudar_lado(self, ladoa,ladob):
        self.LadoA = ladoa
        self.LadoB = ladob
        print(self.LadoA, self.LadoB)
    def exibir_valor(self):
        print('Lado A:', self.LadoA)
        print('Lado B:', self.LadoB)
    def area(self):
        area1 = self.LadoA*self.LadoB
        print('Area:', area1)
    def perimetro(self):
        Perimetro = (2 *self.LadoA) + (2*self.LadoB)
        print("Perimetro: ", Perimetro)
    
        