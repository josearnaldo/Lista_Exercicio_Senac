class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def aumento(self,aumento):
        salario_antigo= self.salario
        self.salario = self.salario +((aumento/100)*self.salario)
        print(f'Salario antigo: {salario_antigo}')
        print(f'Salario novo: {self.salario}')