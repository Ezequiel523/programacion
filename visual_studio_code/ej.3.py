salida =[]
numero = input("Introduce un número: ")

for posicion in range(len(numero)-1, -1, -1):
    salida.append(numero[posicion])
print("El número al revés es: ", salida)

