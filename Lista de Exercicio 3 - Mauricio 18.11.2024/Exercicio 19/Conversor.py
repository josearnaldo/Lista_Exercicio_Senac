class Conversor:
    #dolar em reais
    def __init__(self, dolaremreais, dolar):#domaremreais é a razão, e dolar é a quantidade que tem
        self.dolaremreais = dolaremreais
        self.dolar = dolar
    def converter(self):
        print(f'Em reais{self.dolaremreais *self.dolar}')
