'''
(1 punto) Coge el primer ejercicio (el de edad) y controla valores invá lidos
EDAD: hola
Valor no válido
'''

# Intento realizar lo que hay entre try y except
try:
    # Pido al usuario su edad
    edad = int(input("EDAD: "))

    # Si la edad es superior o igual a 18
    if edad >= 18:
        # Digo por pantalla que es mayor de edad
        print("Mayor de edad")
    else:
        # En caso contrario, es menor de edad
        print("Menor de edad")
        
# Si se desencadena un error, lo controlo
except:
    # Muestro un mensaje formal
    print("Valor no válido")