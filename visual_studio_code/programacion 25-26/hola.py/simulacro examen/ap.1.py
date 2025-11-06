print("========================================================== ")
print("A) Añadir cliente ")
print("V) Validar emails almacenados ")
print("C) Controlar clientes de un dominio ")
print("M) Mostrar los % de los clientes premium y normales ")
print("G) Salir ")
print("========================================================== ")

eleccion = input("Selecciones una de las opciones: ")

while eleccion != "G":
    if cliente != "S" or "N":
        cliente = input(" ¿ Usted es premium ? (S/N): ")
        correo = input("dame un correo: ")
    while cliente != "S" or "N":
       print(" ¿ Usted es premium ? (S/N): ")
eleccion = input("Selecciones una de las opciones: ")

print(" Salir ")
