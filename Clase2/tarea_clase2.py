num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print(f"Ambos números ({num1} y {num2}) son pares.")
elif num1 % 2 == 0:
    print(f"El primer número ({num1}) es par.")
elif num2 % 2 == 0:
    print(f"El segundo número ({num2}) es par.")
else:
    print(f"Ninguno de los dos números ({num1} y {num2}) es par.")
