class Estoque:
    def __init__(self, estoque):
        self.estoque = estoque
    def adicionar(self, adicionar):
        self.estoque = self.estoque+adicionar
        print(f'Estoque adicionado agora tem: {self.estoque}')
    def retirar(self, subtrair):
        self.estoque = self.estoque - subtrair
        print(f'Livros retirados, agora tem:{self.estoque} ')
    def exibir(self):
        print(f'Agora tem {self.estoque}')
        
    
    