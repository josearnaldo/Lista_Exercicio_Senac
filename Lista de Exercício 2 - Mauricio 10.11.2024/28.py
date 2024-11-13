def remove_multiplos(lista, n):
    for i in range(len(lista)-1, -1, -1):
        if(n%lista[i]==0):
            lista.remove(lista[i])
    return lista
lista = [ 1, 2, 3, 4, 5, 6]
n= 8
print(remove_multiplos(lista,n))
            
        