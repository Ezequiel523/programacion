a, b, c = map(int, input("Introduce tres números separados por espacio: ").split())

while not (a == 0 and b == 0 and c == 0):

    if a < b < c:
        print("creciente")
    elif a > b > c:
        print("decreciente")
    else:
        print("desordenados")

    a, b, c = map(int, input("Introduce tres números separados por espacio: ").split())

print("fin")
