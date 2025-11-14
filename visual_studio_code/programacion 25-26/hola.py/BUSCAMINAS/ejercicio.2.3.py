import random
tablero = []
contador = 0
puntuacion = 0
elemento = len(tablero)
print("T) Pulse T para generar un nuevo tablero. ")
print("J) Pulse J para jugar. ")
print("E) Pulse E para salir del juego. ")
opcion = input("Elige una opción: ").upper()

while opcion !="E" :
    if opcion == "T":
        print("generando tablero...")

        for elemento in range(8):
            elemento = (random.randint(0,1))

            if elemento == 0:
                tablero.append("")
            elif elemento == 1:
                contador +=1
                tablero.append("X")
        print("¡Tablero generado!Se han escondido",contador,"Tablero:",tablero)
        opcion = input("Elige una opción: ").upper()
    elif opcion == "J": 
            print("jugando...")
            pos= input("elige una posicion:")
            if elemento ==1:
                puntuacion -=1
                elemento -=1
            print("¡MINA! +1 punto.[Puntuacion:", puntuacion," | Minas restantes", elemento,"]")
            if elemento == 0:
                puntuacion +=1
                elemento -=1
            print("Agua...-1 punto.[Puntuacion:",puntuacion,"| Minas restantes:",elemento,"]" )
            opcion = input("Elige una opción: ").upper()
        
    elif opcion == "E":
        print("saliendo...")
            
    while opcion != "T" and opcion != "J" and opcion != "E":
            print("respuesta incorrecta:")
            opcion = input("Elige otra opción: ").upper()