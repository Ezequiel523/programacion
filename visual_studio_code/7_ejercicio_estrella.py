num = int(input("dime un numero:"))
numFilas = "*"
for numFilas in range (num):
    if numFilas %2 == 0:
        cadena = "*"+"#"*(num-2)+"*"
        print(cadena)
    else:
        cadena = "*"+"@"+"*"+"@"+"*"
        print(cadena)