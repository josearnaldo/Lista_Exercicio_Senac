def soma_naturais(n):
    if n<=0:
        return 0
    return n + soma_naturais(n-1)
print(soma_naturais(-1))


#No conjunto dos Naturais não permite números negativos