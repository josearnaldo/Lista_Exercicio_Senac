from calculadora import Calculadora


print('Calculadora Simples')
numero1 = float(input('Digite o número 1: '))
operacao = input('Digite + para somar e - para subtrair: ')
numero2 = float(input('Digite o número 2: '))
if operacao == '+':
    Calculadora.soma(numero1, numero2)
elif operacao == '-':
    Calculadora.subtracao(numero1, numero2)
else:
    print('Operação invalida')
    
