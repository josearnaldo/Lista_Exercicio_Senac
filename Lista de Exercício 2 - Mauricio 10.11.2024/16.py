def busca_binaria(lista, elemento):
    esquerda = 0
    direita = len(lista) - 1
    
    while esquerda <= direita:
        meio = (esquerda + direita)//2
        

        if lista[meio] == elemento:
            return 'Foi encontrado'  
        elif lista[meio] < elemento:
            esquerda = meio + 1 
        else:
            direita = meio - 1 
    return 'não foi encontrado'
  
lista = [1, 3, 5, 100]
elemento = 9
print(busca_binaria(lista,elemento))

