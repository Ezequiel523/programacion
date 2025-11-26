matriz =[[22, 20, 19, 21], [18, 25, 23, 22], [19, 21, 20, 24], [17, 23, 22, 19], [24, 23, 27, 26]]

def calculaMedia (listaNumeros):
    media = 0
    for numero in listaNumeros:
        media = media + numero
    media = media / len(listaNumeros)
    return media

def calculaMediaFila(matriz):
    listaMedias = []
    for fila in matriz:
        media_fila = calculaMedia(fila)
        listaMedias.append(media_fila)
    return listaMedias

def columna(numColumna, matriz):
    columna = []
    for i in range (len(matriz)):
        columna.append(matriz[i][numColumna])
    return columna

lista_numeros = matriz[0]
resultado = calculaMedia(lista_numeros)
print(resultado)

listaMedias = calculaMediaFila(matriz)
print(listaMedias)

primera_col = columna(0, matriz)
media_primera_columna = calculaMedia(primera_col)
print(media_primera_columna)
