def generaLista():
    lista = []
    num = int(input("dime un número entero: "))
    lista.append(num)
    print(lista)
    return lista

def esValida(lista):
    esV = True
    if True  >= 0:
        num = int(input("dime un número entero: "))
    return esV

def calculaPuntos(lista):
    num = int(input("dime un numero entero: "))
    puntos = len(lista)
    if num > 0:
        print(lista)
    return puntos

listaNotas = generaLista()
if esValida(listaNotas):
    puntos = calculaPuntos(listaNotas)
    print("Secuencia válida. Nº de puntos: ", puntos)
else:
    print("Secuencia de notas NO válidas")