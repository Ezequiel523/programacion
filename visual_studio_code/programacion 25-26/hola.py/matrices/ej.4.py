matriz = [[8, 1, 6],[3, 5, 7],[4, 9, 2]]

def paresLista(lista):
    pares = []
    #TODO
    return pares

def paresMetriz(matriz):
    pares = []
    for i in range(0, len(matriz)):
        fila = matriz[i]
        paresFila = paresLista(fila)
        pares = pares + paresFila
    return pares