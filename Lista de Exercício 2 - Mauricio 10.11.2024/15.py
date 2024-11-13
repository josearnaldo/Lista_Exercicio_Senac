def multiplica_matrizes(matriz1, matriz2):
    lin1 = len(matriz1)
    col1 = len(matriz1[0])
    lin2 = len(matriz2)
    col2 = len(matriz2[0])
    matriz_resultante = []
    mult = []
    soma = 0
    if(lin1 != col2):
        return 'Impossivel de fazer'
    else:
        for i in range(0, lin1):
            mult =[]
            for j in range(0, col2):
                for k in range(0, col1):
                    soma += matriz1[i][k]*matriz2[k][j]
                mult.append(soma)
                soma = 0
         
            matriz_resultante.append(mult)
    return matriz_resultante
matriz1 = [[1,1],
            [1,2]]
matriz2 = [[1,1,1,1],
            [1,1,1,1]]
print(multiplica_matrizes(matriz1, matriz2))