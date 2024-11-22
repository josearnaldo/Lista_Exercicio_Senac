class Agenda:
    def __init__(self, lista):
        self.lista = lista
    def adicionar(self, nome, telefone, email):
        self.lista.append([nome,telefone,email])
    def exibir_lista(self):
        for i in range(0, len(self.lista)):
            for j in range(0,3):
                print(self.lista[i][j], end="  ")
            print()
                