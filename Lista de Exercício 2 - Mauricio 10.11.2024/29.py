def intervalo_entre_elementos(lista):
    minimo = lista[0]
    maximo = lista[1]
    for i in range(0, len(lista)):
        if(lista[i]<minimo):
            minimo = lista[i]
        elif(lista[i]>maximo):
            maximo = lista[i]
    return maximo- minimo
lista=[1,3,2,4,100]
print(intervalo_entre_elementos(lista))