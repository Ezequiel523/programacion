matriz = [[8, 1, 6],[3, 5, 7],[4, 9, 2]]

def devuelveDiagonal1(matriz):
    linea = 0 
    posi = 0
    listaDiagonal1 = []
    for i in range(len(matriz)):
        listaDiagonal1.append(matriz[linea][posi])
        linea += 1
        posi += 1
    return listaDiagonal1
print(devuelveDiagonal1(matriz))

def devuelveDiagonal2(matriz):
    linea = 0 
    posi = len(matriz)-1
    listaDiagonal1 = []
    for i in range(len(matriz)):
        listaDiagonal1.append(matriz[linea][posi])
        linea += 1
        posi -= 1
    return listaDiagonal1
print(devuelveDiagonal2(matriz))