def multiplica_pares(lista):
    multiplicar = 1
    for i in range(0,len(lista)):
        if(lista[i]%2 ==0):
            multiplicar *= lista[i]
    return multiplicar
lista=[1,2,3,4,5,6]
print(multiplica_pares(lista))