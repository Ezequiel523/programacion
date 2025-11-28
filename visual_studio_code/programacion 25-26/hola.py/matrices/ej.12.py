filas = 4
columnas = 5

def crearMatriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for columna in range(columnas):
            fila.append(i+ columna)
        matriz.append(fila)
    return matriz   

matrizcompleta = crearMatriz( filas, columnas)
print(matrizcompleta) 
                                         
