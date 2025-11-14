print("=================================")
print("    SOMBRERO SELECCIONADOR   ")
print("=================================")
print("1. Seleccionar casa para un alumno ")
print ("2. Moestrar estadísticas")
elig =""
while elig != "1" and elig !="2":
    elig = input("Elige una opción. Si quieres salir del programa, escribe la opción 1 y el nombre del personaje innmbrable.")
if elig == "1":
    print(" Ejecutando y seleccionando casa")
else:
    print("Ejecutando y mostrando estadísticas")
nom = input("nombre del alumno: ")
import random
casa = input("Gryffindor -> 1, Slythenrin -> 2 o Hufflepuff -> 3, Ravenclaw -> 4 :")
num = random.randint(1, 4)
print("El Sombrero dice que", nom, "pertenece a", casa)