num = input("Dame un numero: ")
salida = ""
pos = int(input("que posicion quieres saber: "))

if pos < len(num):
    print(num[pos])
else:
    print("posicion incorrecta")
    
