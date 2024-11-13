def intersecao_listas(lista1, lista2):
    intersecao = []
    for i in range(0,len(lista1)):
        for j in range(0,len(lista2)):
            if lista1[i] == lista2[j]:
                intersecao.append(lista1[i])
    return intersecao
lista1=[1,2,3,4,5,6,7,8]
lista2=[2,3,4,5,6,10,11,12]
print(intersecao_listas(lista1,lista2))