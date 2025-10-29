print("1-Azul,2-Roja,3-Verde,4-Rosa,5-Gris")
respuesta = int(input("Dime que habitacion quieres ver"))

match respuesta:
        case 1:
            print("2 camas,primera")
        case 2:
            print("1, primera")
        case 3:
            print("3, segunda")             
        case 4:
            print("2,segunda") 
        case 5:
            print("1, terera")                   