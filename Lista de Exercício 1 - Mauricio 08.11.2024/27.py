def elementos_unicos(lista):
    unicos = []
    for elemento in lista:
        if lista.count(elemento) == 1:
            unicos.append(elemento)
    return unicos

lista = [1,1,2,3,4,5]
print(elementos_unicos(lista))