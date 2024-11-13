def selection_sort(lista):
    minimo = lista[0]
    position = 0
    for i in range(0,len(lista)-1):
        minimo = lista[i]
        position = i
        for j in range(i+1,len(lista)):
            if lista[j]<minimo:
                minimo = lista[j]
                position = j
        if(lista[i]>minimo):
            aux = lista[i]
            lista[i] = minimo
            lista[position] = aux
        
            
            
    return lista
print(selection_sort([4, 3, 23, 5, 0, -1, 24, 150, 200, 100, 100, 400]))