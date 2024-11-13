def conta_palavras(texto):
    lista = texto.split()
    return len(lista)
    
texto = 'Abacate melancia'
print(conta_palavras(texto))