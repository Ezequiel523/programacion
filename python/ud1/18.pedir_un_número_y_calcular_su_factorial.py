num = int(input("Dame un número:"))
resultadoFactorial = num
for numVeces in range(num,0,-1):
    print(numVeces,"*", resultadoFactorial)
resultadoFactorial = resultadoFactorial * numVeces
print(resultadoFactorial)
print("fin")