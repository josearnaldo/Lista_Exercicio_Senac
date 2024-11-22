class Elevador:
    def __init__(self, andar):
        self.andar = int(andar)
    def subiu(self):
        self.andar+=1
        print('Subiu')
        print(f'Andar atual {self.andar}')
    def desceu(self):
        self.andar-=1
        print('Desceu')
        print(f'Andar atual {self.andar}')