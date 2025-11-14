num1 = int(input("dime el primer numero:"))
num2 = int(input("dime el segundo numero:"))
if num2 != 0:
    result = num1/num2
    print("el resultado es:", result)
else:
    if num2 == 0:
        print("no se puede hacer la división.")