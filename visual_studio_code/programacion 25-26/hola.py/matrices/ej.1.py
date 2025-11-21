matriz = [[8, 1, 6],[3, 5, 7],[4, 9, 2]]

def posNum(matriz):
    pos_fila = int(input("introduce la fila: "))
    pos_colum = int(input("introduce la columna: "))
    posicion = matriz[pos_fila][pos_colum]
    return posicion

def filacompleta(matriz):
    pos_fila = int(input("introduce la fila: "))
    fila_completa = matriz[pos_fila]
    return fila_completa

def columnaCompleta(matriz):
    pos_colum = int(input("introduce la columna: "))
    lista = []
    for i in range(0, len(matriz)):
        columna_completa = matriz[i][columna_completa]
        lista.append(columna_completa)
    return lista

posicion = posNum(matriz)
print(posicion)
fila = filacompleta(matriz)
print(fila)
columna = columnaCompleta(matriz)
print(columna)