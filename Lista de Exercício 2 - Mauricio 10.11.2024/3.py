def  conta_consoantes(texto):
    consoantes = "bcdfghjklmnpqrstvwxyz"
    cont = 0
    for i in range(0,len(texto)):
        for j in range(0,len(consoantes)):
            if consoantes[j] == texto[i].lower():
                cont = cont+1
    return cont
print(conta_consoantes('FELIZ'))