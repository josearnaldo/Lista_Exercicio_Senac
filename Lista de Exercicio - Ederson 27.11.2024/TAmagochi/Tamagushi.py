class Tamagushi:
    def __init__(self, nome,fome,saude,idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.energia = 5
    #Humor Calculado
    #Retornar Humor
    def Alterar_nome(self, novo_nome):
        print('Antigo Nome : ', self.nome)
        self.nome = novo_nome
        print('Novo nome: 'self.nome)
    def Retornar_nome(self):
        print(self.nome)
    def Retornar_Fome(self ):
        print(self.fome)
    def Retornar_Saude(self):
        print(self.saude)
    def Retornar_Idade(self):
        print('IDAde Alterada')
        self.idade = nova_idade