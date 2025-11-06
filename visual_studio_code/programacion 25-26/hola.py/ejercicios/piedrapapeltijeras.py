import random
numero =str(input("piedra -> 1, papel -> 2 o tijeras -> 3:"))
maquina = random.randint(1,3)
match numero:
    case 1:
        match maquina:
            case 1:
                print("Empate")
            case 2:
                print("Gana la maquina")
            case 3:
                print("Gana el humano")
    case 2:
        match numero:
            case 1:
                print("Gana el humano")
            case 2:
                print("Empate")
            case 3:
                print("Gana la maquina")
    case 3:
        match numero:
            case 1:
                print("Gana la maquina")
            case 2:
                print("Gana el humano")
            case 3:
                print("Empate")
