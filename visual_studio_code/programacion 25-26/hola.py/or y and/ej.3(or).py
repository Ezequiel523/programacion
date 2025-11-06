gastado=int(input("¿cuantos has gastado?"))
vip=(input("¿eres vip?"))
si_es_vip=True
print(si_es_vip,type(si_es_vip))
if vip=="si": 
    vip=True
else:
    vip=False
if gastado > 100 or vip==True:
    print("tienes descuento")
else:
    print("no tiene descuento")