("nombre": "Azul", "camas": 2, "planta": "Primera"):
("nombre": "Roja", "camas": 1, "planta": "Primera"):
("nombre": "Verde", "camas": 3, "planta": "Segunda"):
("nombre": "Rosa", "camas": 2, "planta": "Segunda"):
("nombre": "Gris", "camas": 1, "planta": "Tercera"):

print("Listado de habitaciones de la Casa Rural:\n")
for num, datos in habitaciones.items():
        print(f"{num}. {datos['nombre']} - {datos['camas']} camas - Planta {datos['planta']}")
num_habitacion = int(input("\nIntroduce el número de habitación (1-5): "))
if num_habitacion in habitaciones:
     datos = habitaciones[num_habitacion]
print(f"\nLa habitación {num_habitacion} ({datos['nombre']}) "
          f"está en la planta {datos['planta']} y tiene {datos['camas']} camas.")
else:
print("Esa habitación no existe.")