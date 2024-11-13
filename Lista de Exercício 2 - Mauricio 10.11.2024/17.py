def  intercala_listas_ordenadas(lista1, lista2):
    lista3=[]
    for i in range(0,len(lista1)):
        lista3.append(lista1[i])
    for j in range(0,len(lista2)):
        lista3.append(lista2[j])
    
    for i in range(0, len(lista3)):
        for j in range(i,len(lista3)):
            if(lista3[i]>lista3[j]):
                aux = lista3[j]
                lista3[j]= lista3[i]
                lista3[i]= aux
                
    return lista3
            

lista1=[1,2,3,4,5,6]
lista2=[2,3,4,8,9,10,7]
print(intercala_listas_ordenadas(lista1,lista2))

