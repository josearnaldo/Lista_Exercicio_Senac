def max_min(lista):
    #return max(lista)-min(lista)
    maximo = lista[0]
    minimo = lista[0]
    for i in range(0, len(lista)):
        if(maximo < lista[i]):
            maximo = lista[i]
        else:
            minimo = lista[i]
    return maximo-minimo
lista=[1,2,3,4,5,6,7,8,9,10]
print(max_min(lista))