'''
Bucle For
'''

for i in [6, 8, 9, 4, 7, True, "Hola", [0,1,2]]:
    print(f"Datos: {i}")
    print(f"Datos: {i}")

print("-----------------------------")

data = ["futbol", "Pc", 18.6, 18, [6,7,10.5],True, False]
for i in data:
    print(f"Datos: {i}")

print("------------FOR Range-----------------")
for i in range(0, 20): 
    print(f"Numero: {i}")

print("------------While-----------------")
numero = 0
while numero < 20:
    print("El numero es: ", numero)
    numero += 1
