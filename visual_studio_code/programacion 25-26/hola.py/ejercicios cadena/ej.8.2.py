nomAp = input("Introduce una frase: ")
palabras = nomAp.split()
resultado = []

for palabra in palabras:
        if len(palabra) == 1:
            nueva = palabra.upper()
        else:
            nueva = palabra[0].upper() + palabra[1:-1].lower()
        resultado.append(nueva)

frase_final = " ".join(resultado)
print(frase_final)
