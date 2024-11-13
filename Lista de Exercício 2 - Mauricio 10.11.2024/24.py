def numeros_primos(n):
    cont =0
    lista = []
    if n==1:
        return 'numero 1 não é primo'
    for i in range(2,n+1):
        cont = 1
        for j in range(2, int(i**(1/2))):
            if(i%j==0):
                cont = cont + 1
        if(cont <2):
            lista.append(i)
    return lista
print(numeros_primos(50))