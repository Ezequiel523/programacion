def leer_num ():
    numeros = []
    contador = 0 

    while contador < 10:
        num = int(input(num))
        contador = contador + 1
    return numeros

def numeros_terminan_en_3(lista_numeros):
    resultado = []
    for num in lista_numeros:
        if num == 3:
            resultado.append(num)
    return resultado

lista = leer_num()
lista_3 = numeros_terminan_en_3(lista)
print("Numeros que terminan en 3:", lista_3)