matriz = [[8, 1, 6],[3, 5, 7],[4, 9, 2]]
pares = []
def numerosPares(matriz):
    for fila in matriz:
        for elemento in fila:
            if elemento % 2 == 0:
                pares.append(elemento)
    return pares
print(numerosPares(matriz))