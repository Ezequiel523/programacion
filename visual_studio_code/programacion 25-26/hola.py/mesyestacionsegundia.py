mes = int(input("Ingrese el número del mes (1-12)"))
dia = int(input("Ingrese el día del mes"))
print(mes)
print(dia)
if (mes == 3 and dia >= 20) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
     print("Primavera")
elif (mes == 6 and dia >= 20) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print("Verano")
elif (mes == 9 and dia >= 20) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print("Otoño")
elif (mes == 12 and dia >= 20) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
       print("Invierno")
else:
        print("Fecha inválida")
