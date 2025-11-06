listaMeses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", " Junio", 
              " Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", " Diciembre"] 
listaTemp=[]
num = "*"
for i in range(0,12):
    temp= int(input("digame la temperatura media de cada mes: "))
    listaTemp.append(temp)
for i in range(0,12):
    print(listaMeses[i],":(", listaTemp[i],"ºC)")
    num= "*"*listaTemp[i]
    print(num)
