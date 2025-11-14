#1º apartado
# Se crean las listas vacías y un contador
listPal = []      # Guardará todas las palabras introducidas
empezar = []      # Guardará las palabras que empiezan con la letra dada
contener = []     # Guardará las palabras que contienen la letra dada
contador = 0      # Contador de palabras

letra = input("Dame una letra: ").lower()   # el .lower es para convertir a minúscula
print("Introduce palabras, escribe stop si no deseas guardar más palabras.")
palabra = input("Dime una palabra: ").lower()

#se crea un bucle para pedir palabras hasta que el usuario escriba "stop"
while palabra != "stop":
    listPal.append(palabra)   # Se agrega la palabra en la lista
    contador += 1             # Se suma 1 al contador
    palabra = input("Dime una palabra: ").lower()  


print("Fin del programa, las palabras dichas con la letra", letra, "son:", listPal)
#2º apartado
print("MENÚ DE OPCIONES: ")
print("Introduzca E si desea devolver la lista de palabras que comienzan por la letra.")
print("Introduzca C si desea devolver la lista de palabras que contienen la letra.")
print("Introduzca S para terminar el programa.")
#5º apartado 
print("Introduzca la letra L si desea obtener la palabra más larga y la palabra más corta")

opcion = input("Elige una opción: ")
# se crea un bucle para seguir ejecutando opciones hasta que el usuario escriba "S"
while opcion != "S":

    if opcion == "E":
        for palabra in listPal:
            if palabra[0] == letra:
                empezar.append(palabra)
        print("Palabras que empiezan con la letra", letra, ":", empezar)

    elif opcion == "C":
        for palabra in listPal:
            if palabra[0] != letra:
                contener.append(palabra)
        print("Palabras que contienen la letra", letra, ":", contener)

    
    if opcion == "L":
        if len(listPal) > 0:
            palaCort = listPal[0]
            palaLag = listPal[0]

            for palabra in listPal:
                if len(palabra) < len(palaCort):
                    palaCort = palabra
                if len(palabra) > len(palaLag):
                    palaLag = palabra

            print("La palabra más corta es:", palaCort)
            print("La palabra más larga es:", palaLag)

    opcion = input("Elige una opción: ")

print("Salir del programa")
