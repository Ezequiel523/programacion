a = int(input("Número: "))

while a != 0:  
    b = int(input("Número: "))
    
    if b == 0:  
        print("fin")
    
    c = int(input("Número: "))
    
    if c == 0: 
        print("fin")

    if a < b < c:
        print("creciente")
    elif a > b > c:
        print("decreciente")
    else:
        print("desordenados")
    
    a = int(input("Número: "))
