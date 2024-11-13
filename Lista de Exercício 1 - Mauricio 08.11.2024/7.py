def conta_vogais(texto):
    cont =0
    for i in range(0, len(texto)):
        if(texto[i] == 'a' or texto[i] == 'A' or texto[i] == 'e' or texto[i] == 'E' or texto[i] == 'i' or texto[i] == 'I' or texto[i] == 'o' or texto[i] == 'O' or texto[i] == 'u' or texto[i] == 'U' or texto[i] == 'á' or texto[i] == 'Á' or texto[i] == 'é' or texto[i] == 'É' or texto[i] == 'í' or texto[i] == 'Í' or texto[i] == 'ó' or texto[i] == 'Ó' or texto[i] == 'ú' or texto[i] == 'Ú'):
            cont = cont + 1
    return cont
    
    
print(conta_vogais('Lingua'))