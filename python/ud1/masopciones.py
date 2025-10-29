opciones=input("elige un dia")

match opciones:
    case "L" | "l":
        print("lunes")
    case "M" | "m":
        print("martes")
    case "X" | "x":
        print("miercoles")
    case "J" | "j":
        print("jueves")
    case "V" | "v":
        print("viernes")
    case "S" | "s":
        print("sabado")
    case "D" | "d":
        print("domingo")
    case _:
        print("no valido")    