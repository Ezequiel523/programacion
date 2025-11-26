matriz = [[8, 1, 6],[3, 5, 7],[4, 9, 2]]

def sumaFilaPares(matriz):
    suma = 0 
    for numfila in range (len(matriz)):
        if numfila % 2 == 0:
            for elementofila in matriz[numfila]:
                suma = suma + elementofila
    return suma

print("La suma de los numeros de las filas pares es: ", sumaFilaPares(matriz))