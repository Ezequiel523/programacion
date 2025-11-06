diasemana = str(input ("Dime el día de la semana"))
diasemana=diasemana.upper()
match diasemana :
    case "Lunes" | "lunes" | "LUNES":
        print("==============")
        print("   LUNES     ")
        print("==============")
        print("8-9 FOL")
        print("9-10 EDE")
        print("10-11 PROG")
        print("11-11:30 Recre")
        print("11:30-12 Progr")
        print("12-14 BBDD")
        print("==============")
    case "SABADO" | "DOMINGO":
        print("estudio y reflexion")
    case _:
        print("no valido")
