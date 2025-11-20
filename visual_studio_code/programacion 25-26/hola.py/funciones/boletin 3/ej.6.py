def cargaelemento():
    esnumero = True
    listaelemento = []
    while esnumero:
        numeros = input("Introduce numero: ")
        for i in numeros:
            if i not in "0123456789":
                esnumero = False
        
        if esnumero:
            listaelemento.append(int(numeros))
    return listaelemento

def estaordenadaAsc(lista):
    orden = True
    i = 0 
    while i < len(lista)-1 and orden:
        if lista[i] > lista[i + 1]:
            orden = False
        i = i + 1 
    return orden

def estaordenada(lista, ascendente):
    if ascendente:
        print("Está ordenada ascendentemente")
    else:
        print("No está ordenada ascendentemente")

lista1 = cargaelemento()
print(lista1)
ascendente = estaordenadaAsc(lista1)
estaordenada(lista1, ascendente)