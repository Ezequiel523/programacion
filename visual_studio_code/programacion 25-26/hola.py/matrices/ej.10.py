matriz = [[8, 1, 6],[3, 5, 7],[4, 9, 2]]
#TERMINAR
def devuelveDiagonal1(matriz):
    linea = 0 
    posi = 0
    listaDiagonal1 = []
    for i in range(len(matriz)):
        listaDiagonal1.append(matriz[linea][posi])
        linea += 1
        posi += 1
    return listaDiagonal1

def devuelveDiagonal2(matriz):
    linea = 0 
    posi = len(matriz)-1
    listaDiagonal1 = []
    for i in range(len(matriz)):
        listaDiagonal1.append(matriz[linea][posi])
        linea += 1
        posi -= 1
    return listaDiagonal1

cuadrado = True
if True == matriz * matriz:
    print(devuelveDiagonal1(matriz))
    print(devuelveDiagonal2(matriz))
noCuadrado = False
if noCuadrado != matriz * matriz:
    print("FIN")