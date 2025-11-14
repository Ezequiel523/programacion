arboles = []
salir = False
# Bucle principal del programa, se ejecuta mientras salir sea False
while salir == False:
    print("--- Menú ---")
    print("1. Introducir número de árboles y sus datos")
    print("2. Mostrar todos los árboles")
    print("3. Mostrar resumen de información")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        cantidad = int(input("¿Cuántos árboles va a introducir? "))
        
        # Bucle para registrar cada árbol
        for i in range(cantidad):

            tipo = input("Tipo del árbol (A/B): ").upper()  # Convertimos a mayúscula
            while tipo != "A" and tipo != "B":
                tipo = input("Tipo no válido. Introduzca A o B: ").upper()
            
            diametro = float(input("Diámetro del tronco (cm): "))

            altura = float(input("Altura del árbol (m): "))

            if tipo == "B":
                edad = int(input("Edad del árbol (años): "))
                # Guardar todos los datos en la lista arboles
                arboles.append([tipo, diametro, altura, edad])
            else:
                # Guardar solo tipo, diámetro y altura para tipo A
                arboles.append([tipo, diametro, altura])

    elif opcion == "2":
        print("Datos de todos los árboles:")
        # Recorrer la lista de árboles e imprimir cada uno
        for arbol in arboles:
            print(arbol)

    elif opcion == "3":
        # Si no hay árboles registrados, mostrar mensaje y volver al menú
        if len(arboles) == 0:
            print("No hay árboles registrados.")

        altura_max = arboles[0][2]  # Altura del primer árbol
        altura_min = arboles[0][2]  # Altura mínima inicial
        indice_max = 0               # Índice del árbol más alto
        suma_edades_B = 0            # Suma de edades de árboles tipo B
        contador_B = 0               # Contador de árboles tipo B
        contador_altos = 0           # Contador de árboles con altura > 30
        
        # Recorrer cada árbol para calcular estadísticas
        for i in range(len(arboles)):
            
            # Guardar la altura actual
            altura = arboles[i][2]
            
            # Actualizar altura máxima si la altura actual es mayor
            if altura > altura_max:
                altura_max = altura
                indice_max = i  # Guardar índice del árbol más alto
            
            # Actualizar altura mínima si la altura actual es menor
            if altura < altura_min:
                altura_min = altura
            
            # Si el árbol es tipo B, sumar la edad y aumentar el contador
            if arboles[i][0] == "B":
                suma_edades_B += arboles[i][3]
                contador_B += 1
            
            # Contar árboles con altura mayor a 30
            if altura > 30:
                contador_altos += 1
        
        # Calcular media de edad para árboles tipo B
        if contador_B > 0:
            media_edad_B = suma_edades_B / contador_B
        else:
            media_edad_B = 0  # Evitar división por cero si no hay tipo B

        print("Resumen de la información:")
        print("-------------------------")
        print("Altura máxima:", altura_max, "m")
        print("Altura mínima:", altura_min, "m")
        print("Media de edad para árboles tipo B:", round(media_edad_B,1), "años")
        print("Número de árboles con altura > 30 m:", contador_altos)
        print("Árbol con altura máxima:", arboles[indice_max])
        print("-------------------------")
    
    elif opcion == "4":
        print("Salir del programa")
        salir = True  # Cambiamos la variable para terminar el bucle
    
    else:
        print("Opción no válida. Intente de nuevo.")
