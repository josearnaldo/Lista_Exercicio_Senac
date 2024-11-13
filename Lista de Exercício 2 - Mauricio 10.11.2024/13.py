def diferença_elementos_lista(lista):
    lista2 = []
    for i in range(0, len(lista)-1):
        if(lista[i]-(lista[i+1])<0):
            lista2.append((lista[i]-(lista[i+1]))*(-1))
        else:
            lista2.append(lista[i]-(lista[i+1]))
            print(lista2[i])
    return lista2
lista = [1, 4, 9, 6, 3]
print(diferença_elementos_lista(lista))

    
    