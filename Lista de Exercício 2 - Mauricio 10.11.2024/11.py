def produto_escalar(vetor1,vetor2):
    vetor_resultante = []
    resultante = 0
    size = len(vetor1)
    if(len(vetor1) != len(vetor2)):
        return 'Impossivel fazer o produto escalar entre os dois vetores, pois não estão na mesma dimensão'
    else:
        for i in range (0,size):
            vetor_resultante.append(vetor1[i] * vetor2[i])
            resultante += vetor1[i]*vetor2[i]
    return vetor_resultante, resultante
vetor1 = [1,2,3]
vetor2 = [1,2,1]
print(produto_escalar(vetor1,vetor2))