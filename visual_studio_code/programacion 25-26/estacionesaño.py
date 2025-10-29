numMes = input("Dime el numero")
match numMes:
    case "1" | "2" | "3":
        print("invierno")
    case "4" | "5" | "6":
        print("primavera")
    case "7" | "8" | "9":
        print("verano")
    case "10" | "11" | "12":
        print("otoño")
    case _:
        print("no valido")