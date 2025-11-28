matriz = [
    ['A', 'B', 'C', 'D'],    # Fila 1
    ['E', 'F', 'G', 'H'],    # Fila 2
    ['I', 'J', 'K', 'L'],    # Fila 3
    ['M', 'N', 'Ñ', 'O'],    # Fila 4
    ['P', 'Q', 'R', 'S'],    # Fila 5
    ['T', 'U', 'V', 'W'],    # Fila 6
    ['X', 'Y', 'Z', '_']     # Fila 7  (“_” representa el espacio)
]

mensajecif = "21,34,74,21,71,31,61,44,74,34,34,21,23,11,74,13,44,42,74,61,53,11,12,11,32,44,74,72,74,51,21,53,54,31,54,61,21,42,13,31,11"

def descifra(matriz,cadena):
    listaCifrada = cadena.split(",")
    codigoDescifrado = []

    for num in listaCifrada:
        fila = int(num[0]) - 1
        col = int(num[1]) - 1
        codigoDescifrado.append(matriz[fila][col])
        mensaje = " "
        for letra in codigoDescifrado:
            mensaje += letra
    return mensaje

def ciframensaje(listaLetras, letra):
    posicionc = -1 
    return posicionc

def buscaLetraMatriz(matriz,letra):
    posicionf = -1
    posicionc = -1
    encntrado = False
    for i in range(len(matriz)-1):
         fila = matriz[i]
         posicionc = buscaLetraMatriz(fila,letra)
         if posicionc != -1:
              posicionf = i
    return posicionf+posicionc

buscaLetraMatriz=["A","B","C","D"]["C"]
print(descifra(matriz,mensajecif))
print(ciframensaje(matriz,letra="C"))
