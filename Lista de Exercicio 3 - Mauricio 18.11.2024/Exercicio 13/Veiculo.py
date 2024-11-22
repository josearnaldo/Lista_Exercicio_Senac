class Veiculo():
    def __init__(self,modelo,velocidade):
        self.modelo = modelo
        self.velocidade = velocidade
    def aumentar(self, aumento):
        self.velocidade=aumento+self.velocidade
        print(self.velocidade)