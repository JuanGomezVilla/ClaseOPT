'''
(1 punto) Pedir un nombre y utilizando un bucle contar el número de letras
NOMBRE: Fulano
Fulano tiene 6 letras
'''
# Le pido al usuario un nombre e inicio una variable de cantidad a 0
nombre = input("NOMBRE: ")
cantidad = 0

# Para cada letra en el nombre
for letra in nombre:
    # Incremento en 1 la cantidad
    cantidad += 1

# Muestro el resultado por pantalla
print(f"{nombre} tiene {cantidad} letras")