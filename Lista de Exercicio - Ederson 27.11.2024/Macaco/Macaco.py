class Macaco :
    def __init__(self,nome,bucho):
        self.nome = nome
        self.bucho = bucho
        self.listaBucho=[]
        self.listaDigerir=[]
    def comer(self,comida):
        self.listaBucho.append(comida)
        print('O Macaco ', self.nome, ' Comeu : ', comida)
    def verBucho(self):
        for i in range(0, len(self.listaBucho)):
            print('Dentro do bucho tem', self.listaBucho[i])
    def digerir(self):
        for i in range(0,len(self.listaBucho)):
            self.listaDigerir.append(self.listaBucho[i])
        self.listaBucho.clear()
        
        print('Dentro do bucho:', self.listaBucho)
        print('O macaco já digeriu: ', self.listaDigerir)
    