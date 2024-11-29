class Conta_corrente:
    def __init__(self, numero,nome):
        self.numero = numero
        self.nome = nome
        self.saldo = 0
    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        print(f'Seu novo nome é:{self.nome}')
    def deposito(self, adicionar):
        self.saldo = self.saldo + adicionar
        print(self.saldo)
    def saque(self, saque):
        if((self.saldo - saque)<0):
            print('Saque indisponivel por valor')
        else:
            self.saldo = self.saldo - saque
            print(self.saldo)
