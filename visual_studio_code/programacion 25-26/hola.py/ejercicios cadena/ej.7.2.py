nomAp = input(" Digame su nombre y apellidos: ")
palabras = nomAp.split()
palabraSalida = ""
for palabra in palabras:
    print(palabra[0].upper())
    print(palabra[1:])
    palabraSalida = palabraSalida + palabra[0].upper() + palabra[1:] + " "
print(palabraSalida)