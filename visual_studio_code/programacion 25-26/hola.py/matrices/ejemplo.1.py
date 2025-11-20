matriz = [[0,2,4], [1,3,5], [6,8,10]]
print(matriz)
print(matriz[1]) # fila 1
print(matriz[1][1]) # elemento fila 1 columna 1

def sumafila(matriz, numfila):
    suma = 0
    for i in matriz[numfila]:
        suma += i
    print(suma)
    return suma

def sumaMatriz(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += sumafila(matriz, i)
    return suma

listaSuma = sumafila(matriz, 1)
sumaRes = sumaMatriz(matriz)
print(sumaRes)

