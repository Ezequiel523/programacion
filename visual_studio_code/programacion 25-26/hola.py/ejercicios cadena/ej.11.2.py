numero = input(" dame un numero: ")
cadenaConPunto = ""
contador = 0

for i in range(len(numero)-3, -1, -3):
    contador = contador + 3
    cadenaConPunto = "." + numero[i: i + 3] + cadenaConPunto
principio = numero[0: len(numero) -contador]
cadenaConPunto = principio + cadenaConPunto

print(cadenaConPunto)
