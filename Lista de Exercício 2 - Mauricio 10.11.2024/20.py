def  conta_intervalo(lista, inicio, fim):
    cont =0
    for i in range(inicio, fim+1):
        for j in range(0, len(lista)):
            if(lista[j] == i):
                print(i)
                cont = 1 + cont
    return f'São {cont} numeros que estão nesse intervalo  entre {inicio} e {fim} '
lista=[1,2,3,4,5,6,7,8,9]
inicio = 3
fim = 6
print(conta_intervalo(lista, inicio,fim))