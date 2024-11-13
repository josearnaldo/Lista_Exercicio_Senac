def remove_duplicados(lista):
    lista_duplicado = []
    for elemento in lista:
        if elemento not in lista_duplicado:
            lista_duplicado.append(elemento)
    return lista_duplicado
        
        
    
        
lista = [1,2,1,3,1,4,1,5,1]
print(remove_duplicados(lista))