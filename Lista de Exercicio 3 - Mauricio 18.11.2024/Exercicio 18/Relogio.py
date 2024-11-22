class Relogio:
    def __init__(self,horas, minutos,segundos):
        self.horas = str(horas)
        self.minutos = str(minutos)
        self.segudos = str(segundos)
    def exibir_horario(self):
        lista=[self.horas,self.minutos]
        horas = ''
        for i in range(0, len(lista)):
            horas += lista[i]
            if(i>=len(lista)-1):
                horas+= ''
            else:
                horas+=':'
        print(horas)