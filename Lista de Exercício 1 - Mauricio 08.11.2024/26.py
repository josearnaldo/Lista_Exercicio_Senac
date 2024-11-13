def soma_pares(lista):
    lista_duplicado = []
    lista_duplicado2 = []
    for elemento in lista:
        if elemento not in lista_duplicado:
            lista_duplicado.append(elemento)
        else:
            lista_duplicado2.append(elemento)
    return sum(lista_duplicado2)
        
        
    
        
lista = [1,2,1,2,1,4,1,5,1]
print(soma_pares(lista))