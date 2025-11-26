matriz = [[8, 1, 6],[3, 5, 7],[4, 9, 2]]

def num_pares(matriz):
    lista = []
    for i in range(0,len(matriz)):
        fila = matriz[i]
        for e in fila:
            if e % 2 == 0:
                lista.append(e)
    return lista

def sumaFila(lista):
    suma = 0 
    for i in lista:
        suma = suma + i
    return suma

pares = num_pares(matriz)
print(pares)
sumas_pares = sumaFila(pares)
print(sumas_pares)

