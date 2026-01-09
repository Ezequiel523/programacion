matriz = [[8, 1, 6],[3, 5, 7],[4, 9, 2]]

def paresLista(matriz):
    resultado = []
    for fila in matriz:
        sumaFila = 0
        for elemento in fila:
            sumaFila += elemento
        resultado.append(sumaFila)
    return resultado

print (paresLista(matriz))
