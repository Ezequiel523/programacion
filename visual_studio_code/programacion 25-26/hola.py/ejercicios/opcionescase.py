opcion=input ("dame una opcion")

match opcion:
    case "A" | "a":
        print("alta")
    case "C" | "c":
        print("cambio")
    case"B" | "b":
        print("baja")
    case _:
        print("no valido")