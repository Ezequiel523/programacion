num = int(input("dime un número:"))
suma = 0
if num > 0:
    for i in range (1,num +1):
        suma += i 
        print("Estos son los números generados:", i)
    print("La suma de los números son: ", suma)
else:
    print("Aegumento inválido")
print("Fin")