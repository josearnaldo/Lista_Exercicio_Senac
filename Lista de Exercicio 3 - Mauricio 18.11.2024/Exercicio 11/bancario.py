class Conta_bancaria:
    def __init__(self):
        self.saldo = 0
    def depositar(self, deposito):
        if(deposito<0):
            print('Deposito negativo')
        else: 
            self.saldo = self.saldo +deposito
            print(f'Você deposito {deposito}, algora tem em conta {self.saldo}')
    def sacar(self, sacar):
        if(sacar >self.saldo):
            print('Saque maior que o valor em conta')
        else:
            self.saldo = self.saldo-sacar
            print(f'Você sacou {sacar}, agora tem em conta {self.saldo} ')
    def exibir(self):
        print(f'Você tem: {self.saldo}')