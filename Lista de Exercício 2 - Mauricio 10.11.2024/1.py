def multiplicar_escalar(lista, escalar):
    for i in range(0,len(lista)):
        lista[i]  = lista[i] * escalar
    return lista, f'escalar:{escalar}'
lista = [1,10,100,1000,1000000]
escalar = 3

print(multiplicar_escalar(lista,escalar))