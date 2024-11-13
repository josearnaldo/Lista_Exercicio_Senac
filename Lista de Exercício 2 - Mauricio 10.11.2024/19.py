def diagonais_matriz(matriz):
    l = len(matriz)
    c = len(matriz[0])
    if l == c:
        c = c-1
        diagonal_principal= []
        diagonal_secundaria = []
        for i in range(0, l):
            diagonal_secundaria.append(matriz[i][c-i])
            for j in range(0,c+1):
                if(i == j):
                    diagonal_principal.append(matriz[i][j])
        return f'diagonal_principal é {diagonal_principal} , diagonal_secundaria{diagonal_secundaria}'
    else:
        return 'Matriz não é quadrada'
matriz  =[[21,1,3],
        [1,2,1],
        [3,1,2]]
print(diagonais_matriz(matriz))