def inverte_string(s):
    inverte = ''
    for i in range(len(s)-1, -1, -1):
        inverte+= s[i]
    return inverte
    
print(inverte_string('123456789'))