diasemana = input ("Dime el día de la semana")
match diasemana :
    case "Lunes" | "lunes" | "LUNES":
        print("==============")
        print("   Lunes     ")
        print("==============")
        print("8-9 FOL")
        print("9-10 EDE")
        print("10-11 PROG")
        print("11-11:30 Recre")
        print("11:30-12 Progr")
        print("12-14 BBDD")
        print("==============")
    case "Sabado" | "SABADO" | "sabado":
        print("estudio y reflexion")
    case "Domingo" | "domingo" | "DOMINGO":
        print("estudio y reflexion")
    case _:
        print("no valido")
