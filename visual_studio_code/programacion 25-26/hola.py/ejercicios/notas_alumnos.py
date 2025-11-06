nombre = (input("nombre del alumno"))

while nombre != "exit":
    nota=float(input("dime la nota que has obtenido:"))

    if nota >=90 and nota<=100:
        print("sobresaliente")
    elif nota>=70 and nota <=89:
        print("notable")
    elif nota>=60 and nota<=69:
        print("bien")
    elif nota>=50 and nota<=59:
        print("suficiente")
    elif nota>=0 and nota<=49:
        print("suspenso")
    nombre = (input("nombre del alumno"))