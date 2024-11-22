class Jogo:
    def __init__(self, nome ,pontuacao):
        self.nome = nome
        self.pontuacao = pontuacao
    def iniciar_jogo(self):
        print(f'{self.nome } O Jogo Iniciou:')
    def registrar_pontos(self, pontos):
        self.pontuacao = self.pontuacao + pontos
    def exibir_pontuacao(self):
        print(f'{self.nome}, sua pontuacao é {self.pontuacao}')