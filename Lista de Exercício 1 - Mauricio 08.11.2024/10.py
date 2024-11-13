def eh_primo(n):
    
    cont = 0
    if( n == 2 or n ==3 ):
        return 'é primo'
    elif (n == 1 or n == 0):
        return 'não é primo'
    else:
        for i in range(1,int(n**(1/2))+1):
            if(n%i ==0):
                cont = cont+1
        if(cont <= 1 ):
            return 'é primo'
        else:
            return 'não é primo'
            
print(eh_primo(23))