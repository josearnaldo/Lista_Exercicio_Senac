class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def informacoes(self):
        return print('Titulo:',self.titulo,'Autor:', self.autor)
        