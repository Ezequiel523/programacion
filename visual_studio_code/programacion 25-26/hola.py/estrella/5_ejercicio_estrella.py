num = int(input("dime un numero:"))
numFilas = "*"
for numFilas in range (num):
    if numFilas == 0 or numFilas == num-1:
        print("*","#"*(num-2),"*")
    else:
        cadena = "*"*(num)+"*"
        print(cadena)