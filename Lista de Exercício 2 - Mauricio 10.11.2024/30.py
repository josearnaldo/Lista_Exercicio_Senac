def histograma(lista):
    lista_ocorrencia = []
    for elemento in lista:
        if elemento not in [item[0] for item in lista_ocorrencia]:
            count = lista.count(elemento)
            lista_ocorrencia.append((elemento, count))
    return dict(lista_ocorrencia)
lista = [100,2,3,2,100,1,5,6]
print(histograma(lista))
