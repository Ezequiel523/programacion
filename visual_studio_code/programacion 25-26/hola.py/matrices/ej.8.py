matriz = [[8, 1, 6],[3, 5, 7],[4, 9, 2]]

def maxFila(fila):
    fila = 0
    for elemento in fila:
        if elemento > maximo:
            maximo = elemento
    return fila

print (maxFila(matriz))