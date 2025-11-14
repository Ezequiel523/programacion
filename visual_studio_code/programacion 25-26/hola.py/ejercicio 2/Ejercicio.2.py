# empezamos con valores negativos para asegurarnos que el bucle se cumple
num1 = -1
num2 = -2

while num1 != 0 and num2 != 0: #se crea un bucle cuando los dos son distintos de 0
    num1 = int(input("dime el primer numero: "))
    num2 = int(input(" dime el segundo numero: "))
    if num1 >= num2:# si num1 es >= que num2 se realiza esta accion
        print("numeros no validos.")
        num1 = int(input("dime el primer numero: "))
        num2 = int(input(" dime el segundo numero: "))
    elif num1 == 0 and num2 == 0:#si los dos num =0 se hace lo siguiente
         print(" programa terminado ")
    else:#sino ocurre ninguna de la dos acciones anteriores se hace lo siguiente
       impar = []#creamos una lista vacia
       for n in range(num1, num2 +1):#se ponen todos lo numeros incluyendo el ultimo
           if n %2 != 0:#aqui dice que si la n se %2 y es != 0 se añade a la lista
               impar.append(n)
    print("================================================")
    print("Impares que existen entre",num1, "y el", num2,"son:", impar)
    print("En total existen" ,len(impar),"números impares en el rango")
    print("================================================")



