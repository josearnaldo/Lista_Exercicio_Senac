def esta_ordenada(lista):
    for i in range(0, len(lista)-1):
        for j in range(i, len(lista)):
            if (lista[i]>lista[j]):
                return 'Não está ordenada em ordem crescente'
    
    return 'Está ordenada'
lista = [-1,1,2,3,4,5,6]
print(esta_ordenada(lista))