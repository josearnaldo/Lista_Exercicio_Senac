def produto_lista(lista):
    if not lista:
        return 1
    return lista[0] * produto_lista(lista[1:])
lista = [1,2,3]
print(produto_lista(lista))