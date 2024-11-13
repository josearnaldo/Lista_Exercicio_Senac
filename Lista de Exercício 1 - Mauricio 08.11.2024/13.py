def eh_palindromo(s, letra):
    cont = 0
    for i in range(0, len(s)):
        if(s[i] == letra):
            cont = cont+1
    return cont

print(eh_palindromo('abacate', 'a'))
        