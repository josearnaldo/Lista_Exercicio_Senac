def retira_espacos(texto):
    textos=''
    lista = texto.split()
    for i in range(0, len(lista)):
        textos += lista[i]
    return textos
    
print(retira_espacos('Olá Mundo Olá Mundo Olá Mundo Olá Mundo Olá Mundo Olá MundoOlá Mundo Olá Mundo Olá Mundo' ))