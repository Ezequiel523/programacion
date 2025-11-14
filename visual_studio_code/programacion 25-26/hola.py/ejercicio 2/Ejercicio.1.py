registrar = "S"
#definiciones de contadores 
total_incidentes = 0
leves = 0
graves = 0
eso = 0
post = 0

while registrar == "S": #si poner "S" se cumple este bucle
    registrar = input("¿Desea registrar un nuevo incidente? (S/N): ").strip().upper()
#el .strip y el .upper se utilizan para mayusculas y minusculas
    while registrar != "S" and registrar != "N":# se repite el bucle sino se pone ninguna de las dos letras
        print("Respuesta no válida. Por favor, introduzca S o N.")
        registrar = input("¿Desea registrar un nuevo incidente? (S/N): ").strip().upper()

    if registrar == "S": # aqui dice que en caso de "S" se hace eso
        nivel = input("¿En qué nivel ha ocurrido? (E = ESO, P = Post-Obligatoria): ").strip().upper()
        while nivel != "P" and nivel != "E":#se hace un bucle sino se pone ninguna de las dos letras
            print("Entrada no válida. Por favor, introduzca E o P.")
            nivel = input("¿En qué nivel ha ocurrido? (E = ESO, P = Post-Obligatoria): ").strip().upper()

        tipo = input("Tipo de incidente (L = Leve, G = Grave): ").strip().upper()#definimos la funcion
        while tipo != "L" and tipo != "G":#se hace un bucle si no se pone ninguna de las dos letras
            print("Entrada no válida. Por favor, introduzca L o G.")
            tipo = input("Tipo de incidente (L = Leve, G = Grave): ").strip().upper()
        #acciones de los contadores
        total_incidentes += 1#siempre se suma 1 cada vez que le digamos que si a la primera pregunta
        if tipo == "L": # se le suma 1 a leves si se pone "L"
            leves += 1
        else:#se le suma uno a graves sino pone "L"
            graves += 1

        if nivel == "E":#se le añade 1 a eso si pone "E"
            eso += 1
        else:#se le añade 1 a post sino pone "E"
            post += 1

if total_incidentes > 0:#si es >0 se hace lo siguiente
    # dividimos y multiplicamos para que nos de un porcentaje sobre 100%
    por_eso = (eso/total_incidentes)*100
    por_post = (post/total_incidentes)*100

print("Se han producido", total_incidentes," incidentes en el centro: ", leves, "de ellos Leves y", graves," Graves, siendo el", por_eso, "% en ESO y el", por_post, "% en Post-Obligatoria.")
