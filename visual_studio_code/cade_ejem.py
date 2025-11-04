#====================================================
#Las cadenas son inmutables
#====================================================
nombre = "Lucia"
nombre.replace("a", "o")#no cambia la variable nombre
print(nombre)
nombre = nombre.replace("a", "o")#si cambia la variable nombre
#====================================================
#Paso de String a lista: lista(nombreCadena) y de lista a String: for y concateno caracter a caracter
#====================================================
nombreLista = list(nombre) #Paso de String a lista de caracteres
nombreLista.insert(0, "A")
print(nombreLista)
cadenaSalida = ""
for valor in nombreLista: #Paso de lista de caracteres a String
    cadenaSalida = cadenaSalida + valor 
print(cadenaSalida)