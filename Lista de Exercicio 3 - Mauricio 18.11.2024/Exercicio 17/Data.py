class Data:
    def __init__(self, dia,mes,ano):
        self.dia = str(dia)
        self.mes = str(mes)
        self.ano = str(ano)
    def formatar(self):
        lista = [self.dia,self.mes,self.ano]
        data = ''
        for i in range(0,len(lista)):
            data += lista[i] 
            if (i>=len(lista)-1):
                data+= ' '
            else:
                data += '/'
        return print(data)