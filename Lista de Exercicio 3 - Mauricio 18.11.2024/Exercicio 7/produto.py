class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def desconto(self, desconto):
        print('Produto: ', self.nome, 'Preco: ', self.preco )
        return print('Valor com desconto : ', (self.preco- (self.preco *(desconto/100))))
        