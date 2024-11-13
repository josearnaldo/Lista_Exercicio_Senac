def conta_ocorrencia(lista, elemento):
    cont = 0
    for i in range (0, len(lista)):
        if(lista[i] == elemento):
            cont = cont+1
        
    return cont
lista = [1,2,1,3,1,4,1,5,1]
print(conta_ocorrencia(lista, 1))