from Retangulo import Retangulo
retangulo = Retangulo(2,3)

retangulo.perimetro()
retangulo.area()
# Fazer um algoritmo que permita usar a classe
print('Digite o lado')
lado1 = float(input('Escreva o lado A'))
lado2 = float(input('Escreva o lado B'))
retangulo = Retangulo(lado1,lado2)
quadriculado = float(input('Escreva o tamanho do piso quadriculado'))

print('A quantidade de piso é :', (retangulo.area()/quadriculado))