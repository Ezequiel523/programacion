print("T) Pulse T para generar un nuevo tablero. ")
print("J) Pulse J para jugar. ")
print("E) Pulse E para salir del juego. ")
opcion = input("Elige una opción: ").upper()

while opcion == "T" and opcion == "J" and opcion =="E" :
    opcion = input("Elige una opción: ").upper()
    if opcion == "T":
        print("generando tablero...") 
    elif opcion == "J":
        print("jugando...")
    elif opcion == "E":
        print("saliendo...")
    while opcion != "T" and opcion != "J" and opcion != "E":
            print("respuesta incorrecta:")
            opcion = input("Elige otra opción: ")