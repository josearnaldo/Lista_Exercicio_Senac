class Filme:
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao
    def informacao(self):
        print('O titulo é ',self.titulo,' Tempo de duração:', self.duracao)