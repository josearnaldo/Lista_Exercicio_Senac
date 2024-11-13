def media_ponderada(lista_valores, lista_pesos):
    somatorio1 =0
    somatorio2 = 0
    for i in range(0, len(lista_valores)):
        somatorio1 += lista_valores[i]*lista_pesos[i]
        somatorio2 += lista_pesos[i]
    return somatorio1/somatorio2
        
lista_valores = [1,1,1,1,1]
lista_pesos=[2,2,2,2,2]
print(media_ponderada(lista_valores,lista_pesos))
