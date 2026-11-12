'''
(1 punto) Pedir una edad y dice si es mayor/menor de edad
EDAD: 99
Mayor de edad
'''

# Pido al usuario su edad
edad = int(input("EDAD: "))

# Si la edad es superior o igual a 18
if edad >= 18:
    # Digo por pantalla que es mayor de edad
    print("Mayor de edad")
else:
    # En caso contrario, es menor de edad
    print("Menor de edad")