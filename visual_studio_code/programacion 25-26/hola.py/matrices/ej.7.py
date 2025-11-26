matriz = [[8, 1, 6],[3, 5, 7],[4, 9, 2]]

def suma_columnas_pares(matriz):
    suma = 0
    for fila in matriz:
        for i in range(len(fila)):
            if i % 2 == 0:
                suma += fila[i]
    return suma

resultado = suma_columnas_pares(matriz)
print("Suma: ", resultado)