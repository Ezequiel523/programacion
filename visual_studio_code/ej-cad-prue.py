cadena = "Hola"
["H","o", "l", "a"]
if "o" in "Hola":
    posicion = cadena.index("o")

cadena = "Hola caracola"
cadena.split("o") #["H", "la", "carac", "la"]

#"Hola esto es \"
#la \ sirve para pintar caracter y no lo interprete como fin 

for elemento in cadena:
    print(elemento)

for posicion in range(len(cadena)):
    print(cadena(posicion))