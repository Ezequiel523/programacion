ventas = [
    ["Portátil", 150, 799.99, 4.5],
    ["Smartphone", 250, 599.99, 4.3],
    ["Auriculares", 400, 49.99, 4.0],
    ["Tablet", 120, 299.99, 3.9],
    ["Monitor", 180, 199.99, 4.2],
    ["Smartwatch", 220, 149.99, 4.1],
    ["Teclado mecánico", 300, 89.99, 4.4],
    ["Ratón gaming", 350, 59.99, 4.0],
    ["Cámara digital", 90, 999.99, 4.6],
    ["Consola", 200, 399.99, 4.7]
]
nombreProducto = input("dime el nombre producto : ")

def calcularIngresos(ventas, nombreProducto):
    ingresos = 0
    unidades = 0
    precio = 0

    i = 0
    encontrado = False
    while i < len (ventas) and not encontrado:
        if ventas[i][0] == nombreProducto:
            unidades = ventas [i][1]
            precio = ventas [i][2]
            encontrado = True
        else:
            i += 1
    ingresos = unidades * precio
    return ingresos

def getProducto(ventas, nombreProducto):
    producto = []

    i = 0
    encontrado = False

    while i < len(ventas) and not encontrado:
        if ventas[i][0] == nombreProducto:
            producto.append(ventas[i])
            encontrado = True
        else:
            i += 1
    return producto

def numMayores(ventas, nombreProducto):
    mayorlista = []
    if len(ventas) >= "4,2":
        nombreProducto = True
    else:
        nombreProducto = False
    if nombreProducto >= "4,2":
        mayorlista.append(len(ventas))
    return mayorlista


resultado1 = calcularIngresos(ventas,nombreProducto)
print(resultado1)
resultado2 = getProducto(ventas, nombreProducto)
print(resultado2)
