num = int(input("dime un numero:"))
numFilas = "*"
for numFilas in range (num):
    if numFilas == 0 or numFilas == num-1:
        print("*"*num)
    else:
        cadena = "*"+" "*(num-2)+"*"
        print(cadena)

