def trozoDeNumero(numero, inicio, fin):
    num = str(numero)
   
    if inicio < 1 or fin > len(num) or inicio > fin:
        return "Rango inválido"

    trozo = num [inicio - 1:fin]
    return int(trozo)
