cadena = input(" dame una cadena: " )
letra1 = input(" dame un caracteres: " )
while len(letra1) != 1:
    letra1 = input( " dame un caracter: ")

letra2 = input(" dame otro caracter: " )
while len(letra2) != 1:
    letra2 = input(" dame otro caracter:")

if letra1 in cadena:
    salida = cadena.replace(letra1, letra2)
else: 
    salida = ""
print(salida)