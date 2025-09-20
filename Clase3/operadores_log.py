'''
Operadores Lógicos 
'''

a = 30
b = 40
c = 50

r = ((a < b) and (b > c) and (c > a))
print("r: ", r)           # AND

print("-------------------")

r = ((a < b) or (b > c))
print("r: ", r)           # OR

print("-------------------")

r = not(a < b) or (c < a)
print("r: ", r)           # NOT

