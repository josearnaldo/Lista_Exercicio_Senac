def eh_palindromo(s):
    revertido=''
    cont =0
    for i in range ((len(s)-1),-1,-1):
       revertido+= s[i]
    for i in range(0, len(s)):
        if(s[i] == revertido[i]):
            cont = cont+1
    if(len(s) == cont):
        return 'é palindromo'
    else:
        return 'não é palindromo'


print(eh_palindromo('salve'))
        