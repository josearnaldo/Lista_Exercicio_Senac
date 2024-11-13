def quick_sort(lista):
    lado = []
    lado.append((0, len(lista) - 1))  
    while lado:
        inicio, fim = lado.pop()
        if inicio >= fim:
            continue
        u_sublista = lista[fim]
        i = inicio - 1 
        for j in range(inicio, fim):
            if lista[j] <= u_sublista:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
        lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
        lado.append((inicio, i)) 
        lado.append((i + 2, fim))  
    return lista
print(quick_sort([4, 3, 23, 5, 0, -1, 24, 150, 200, 100, 100, 400]))