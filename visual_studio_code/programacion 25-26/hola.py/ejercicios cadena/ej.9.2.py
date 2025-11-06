cadena = input(" dame una cadena: " )
letra1 = input(" dame un caracteres: " )
letra2 = input(" dame otro caracter: " )

if letra1 in cadena:
    salida = cadena.replace(letra1, letra2)
print(salida)
