def concatena_strings(lista_strings):
    texto = ''
    for i in range(0, len(lista_strings)):
        texto += lista_strings[i]
        texto += ' '
    return texto  
lista_strings = ['um dia', 'dois dia', 'três dia', 'leão, rato']
print(concatena_strings(lista_strings))