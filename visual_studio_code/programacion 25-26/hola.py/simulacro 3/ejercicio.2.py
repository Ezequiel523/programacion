# Mandar a la maquina a poner numeros aleatorios
import random

# Variable de control para el bucle de la partida individual
partida_terminada = False

# iniciar un bucle cuando la partida_terminada = a False
while partida_terminada == False:

    # Pedir elección del jugador 1 (humano)
    jugador1_eleccion = input("Jugador 1, elige Par o Non: ").lower()
    while jugador1_eleccion != "par" and jugador1_eleccion != "non":
        jugador1_eleccion = input("Elección no válida. Escribe 'Par' o 'Non': ").lower()

    # Pedir número de dedos del jugador 1
    jugador1_dedos = int(input("Jugador 1, cuántos dedos sacas (0-5): "))
    while jugador1_dedos < 0 or jugador1_dedos > 5:
        jugador1_dedos = int(input("Número no válido. Introduce un número entre 0 y 5: "))

    # Pedir número de dedos del jugador 2 (humano)
    jugador2_dedos = int(input("Jugador 2, cuántos dedos sacas (0-5): "))
    while jugador2_dedos < 0 or jugador2_dedos > 5:
        jugador2_dedos = int(input("Número no válido. Introduce un número entre 0 y 5: "))

    # Calcular suma de dedos
    suma = jugador1_dedos + jugador2_dedos

    # Determinar si es par o impar
    if suma % 2 == 0:
        resultado = "par"
    else:
        resultado = "non"

    # Determinar ganador
    if resultado == jugador1_eleccion:
        print("Jugador 1 ha ganado")
    else:
        print("Jugador 2 ha ganado")

    # Marcar la partida como terminada
    partida_terminada = True

# Inicializar contadores de victorias
victorias_jugador = 0
victorias_maquina = 0

# Variable de control para el bucle del juego indefinido
juego_terminado = False

# Bucle principal hasta que ambos saquen 0
while juego_terminado == False:
    
    # Jugador humano elige Par o Non
    jugador_eleccion = input("Jugador, elige Par o Non: ").lower()
    while jugador_eleccion != "par" and jugador_eleccion != "non":
        jugador_eleccion = input("Elección no válida. Escribe 'Par' o 'Non': ").lower()
    
    # Jugador humano saca dedos
    jugador_dedos = int(input("Jugador, cuántos dedos sacas (0-5): "))
    while jugador_dedos < 0 or jugador_dedos > 5:
        jugador_dedos = int(input("Número no válido. Introduce un número entre 0 y 5: "))
    
    # Máquina saca dedos aleatoriamente entre 0 y 5
    maquina_dedos = random.randint(0,5)
    print("La máquina ha sacado:", maquina_dedos)
    
    # Si ambos sacan 0, terminar el juego
    if jugador_dedos == 0 and maquina_dedos == 0:
        juego_terminado = True  # Cambiar variable de control para salir del bucle
        print("Fin del juego")
        print("Partidas ganadas por el jugador:", victorias_jugador)
        print("Partidas ganadas por la máquina:", victorias_maquina)
    
    else:
        suma = jugador_dedos + maquina_dedos
        if suma % 2 == 0:
            resultado = "par"
        else:
            resultado = "non"

        if resultado == jugador_eleccion:
            print("Has ganado esta partida")
            victorias_jugador += 1
        else:
            print("La máquina ha ganado esta partida")
            victorias_maquina += 1
