numVeces = 9999
longitudLista = 15
while numVeces > longitudLista:
    numVeces = int(input("dame el numero de veces a rotar: "))

lista = []
for i in range(longitudLista):
    numero = int(input("dame el numero: "))
    lista.append(numero)
print(lista)
listaSalida = []
listaDetras = lista[0:len(lista)-numVeces]
print(listaDetras)
for posicion in range(1, numVeces,+1):
    elemento = lista[len(lista)-posicion]
    listaSalida.insert(0 ,elemento)
listaSalida = listaSalida + listaDetras
print(listaSalida)