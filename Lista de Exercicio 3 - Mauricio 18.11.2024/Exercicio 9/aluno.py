class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    def verificar_nota(self):
        if(self.nota>=7):
            return print('Aluno está aprovado')
        else:
            return print('Aluno está reprovado')