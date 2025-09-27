'''
Introducción a listas en Python
'''

array = ["futbol", "Pc", 18.6, 18, [6,7,10.5],True, False]
print(array)

# Acceder a un elemento de la lista
print(array[0])
print("Pc" in array) 

print(array.index("futbol")) # Devuelve el indice del elemento

print(array.count("Pc")) #Devuelve la cantidad de veces que se repite el elemento

array.clear() # Limpia la lista
print("Array", array)

array = ["futbol", "Pc", 18.6, 18, [6,7,10.5],True, False]
array.reverse() # Invierte la lista
print("Array invertido", array)
