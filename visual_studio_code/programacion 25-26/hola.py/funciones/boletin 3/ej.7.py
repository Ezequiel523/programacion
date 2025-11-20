numcadenas = int(input("¿Cuántas cadenas quieres introducir?: "))
def cargacadenas(numcadenas):
    lista = []
    i = 0
    while i < numcadenas:
        cadena = input("Introduce una cadena: ")
        lista.append(cadena)
        i = i + 1
    return lista

lista = cargacadenas(numcadenas)
print(lista)
#def cadenarepetida(lista):
    