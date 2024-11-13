def desvio_padrao(lista):
    size = len(lista)
    desvio = 0
    u = (sum(lista)/size)
    somatorio = 0
    for i in range(0,len(lista)):
        desvio += ((lista[i]-u)**2)
    return (desvio/size)**(1/2)
lista=[1,2,3,4,5,6,7,8,9,10]
print(desvio_padrao(lista))