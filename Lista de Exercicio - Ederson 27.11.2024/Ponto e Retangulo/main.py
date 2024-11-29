from Ponto import Ponto
from Retangulo import Retangulo
x=1
y=1
ponto1 = Ponto(x,y)

Retangulo(10,10,x,y)

print('Escolha uma opcao')
print('1 - mudar valores do retangulo')
print('2 - Imprimir o Centro')
escolha = int(input('Escolha: '))

if(escolha ==  1):
    largura = int(input('Escolha a LArgura do Retangulo'))
    altura = int(input('Escolha a Altura do Retangulo'))
    x = int(input('Escolha o Ponto x que comece o retangulo'))
    y = int(input('Escolha o ponto y que comece o retangulo'))
    retangulo = Retangulo(largura,altura,x,y)
elif(escolh == 2):
    retangulo.centro()
else:
    return 'Opcao invalida'
    