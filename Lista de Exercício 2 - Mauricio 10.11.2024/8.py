def insertion_sort(lista):
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > atual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = atual
    return lista

print(insertion_sort([4, 3, 23, 5, 0, -1, 24, 150, 200, 100, 100, 400]))
