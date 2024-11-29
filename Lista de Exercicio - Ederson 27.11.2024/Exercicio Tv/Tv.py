class Tv :
    def __init__(self, canais, volume):
        self.canal = ['canal 1', 'canal 2', 'canal 3 ', 'canal 4']
        self.canal_atual = 'canal 1'
        self.canal[canais]
        self.volume = volume
    def mudar_canal(self, numero_canal):
        
        if((len(self.canal) <numero_canal) or (len(self.canal)<0)):
            print('canal Inexistente')
            print('VocÊ ainda está no mesmo canal', self.canal)
        else:
            self.canal_atual = self.canal[numero_canal]
            print('Canal Atual é :',self.canal_atual)
            
    def aumentar_volume(self, numero_volume):
        if(self.volume+numero_volume > 100 or self.volume <0):
            print('volume Inexistente')
        else:
            self.volume = self.volume+numero_volume
        print('Volume Atual:', self.volume)
    def diminuir_volume(self, numero_volume):
        if(self.volume-numero_volume  <0 or numero_volume < 0):
            print('Volume Incorreto')
            print(self.volume)
        else:
            self.volume = self.volume - numero_volume 
    # def aumentar_volume():
    # def diminuir_volume():