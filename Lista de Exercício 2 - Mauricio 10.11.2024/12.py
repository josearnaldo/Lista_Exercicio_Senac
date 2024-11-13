def separa_pares_impares(lista):
    par = []
    impar = []
    for i in range(0, len(lista)):
        if(lista[i]%2==0):
            par.append(lista[i])
        else:
            impar.append(lista[i])
    return f'lista par: {par} lista impar: {impar}'
lista = [1,2,3,4,5,6,7,8,9]
print(separa_pares_impares(lista))