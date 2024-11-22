class Banco:
    def __init__(self):
        self.lista = []
    def adicionar_conta(self, nome, saldo):
        self.lista.append([nome, saldo])
    def listar_contas(self):
        for i in range(0,len(self.lista)):
            print(f'Titular: {self.lista[i][0]}, Saldo: {self.lista[i][1]:.2f}')
        