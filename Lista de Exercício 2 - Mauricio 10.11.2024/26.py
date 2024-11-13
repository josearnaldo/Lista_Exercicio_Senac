def merge_sort(lista):
    tamanho = len(lista)
    intervalo = 1
    while intervalo < tamanho:
        for inicio in range(0, tamanho, intervalo * 2):
            meio = inicio + intervalo
            fim = min(inicio + intervalo * 2, tamanho)
            esquerda = lista[inicio:meio]
            direita = lista[meio:fim]
            i = j = 0
            for k in range(inicio, fim):
                if i < len(esquerda) and (j >= len(direita) or esquerda[i] <= direita[j]):
                    lista[k] = esquerda[i]
                    i += 1
                else:
                    lista[k] = direita[j]
                    j += 1
        intervalo *= 2
    return lista
lista = [2,5,1,30,60,20,100]
print(merge_sort(lista))
