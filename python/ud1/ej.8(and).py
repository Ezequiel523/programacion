puntaje_credito = int(input("Ingrese su puntaje de crédito: "))
ingreso_anual = float(input("Ingrese su ingreso anual en dólares: "))

if puntaje_credito > 700 and ingreso_anual >= 60000:
    print("¡Felicidades! Usted es elegible para el préstamo hipotecario.")
else:
    print("Lo sentimos, no cumple con los requisitos para el préstamo hipotecario.")