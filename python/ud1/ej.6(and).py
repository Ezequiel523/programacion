saldo=float(input("Introduce el saldo de la cuenta:"))
retirada=int(input("Introduce la cantidad que quieres retirar:"))

if retirada>saldo:
    print("No tienes suficiente dinero en la cuenta")

