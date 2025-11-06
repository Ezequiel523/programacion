import funciones
cadena = input("dame una cadena: ")
num = int(cadena)
salida= ""

while len(cadena) <= 4:
    cadena = input("dame una cadena: ")

if num % 2 == 0:
    #salida = cadena[2]+cadena[4]
    ouput = funciones.calculaCadena(2,4,cadena)
    print(ouput)

elif num % 3 == 0:
    #salida = cadena[1]+cadena[2]
    funciones.calculaCadena(1,3,cadena)
elif num % 7 == 0:
    #salida = cadena[0]+cadena[3]
    funciones.calculaCadena(0,3,cadena)
    
