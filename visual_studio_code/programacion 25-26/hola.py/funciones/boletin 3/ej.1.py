import random
lista = []
for i in range(0,5):
    aleatorio = random.randint(0,100)
    lista.append(aleatorio)
print(lista)

def obtengoLista(lista):
    ordenada = True
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            ordenada = False
        else:
            ordenada = ordenada and True
    return ordenada

orden = obtengoLista(lista)
print("")
print(orden)