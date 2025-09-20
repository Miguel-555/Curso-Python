num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print(f"Ambos números ({num1} y {num2}) son pares.")
elif num1 % 2 == 1 and num2 % 2 == 1:
    print(f"Ambos números ({num1} y {num2}) son impares.")
elif num1 % 2 == 0 and num2 % 2 == 1:
    print(f"El primer número ({num1}) es par y el segundo ({num2}) es impar.")
elif num1 % 2 == 1 and num2 % 2 == 0:
    print(f"El primer número ({num1}) es impar y el segundo ({num2}) es par.")
else:
    print("Valores ingresados no correctos.")

print("Fin del Programa")
