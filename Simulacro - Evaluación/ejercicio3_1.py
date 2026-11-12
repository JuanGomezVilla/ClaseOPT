'''
(1 punto) Una batería tiene una carga desconocida, cárgala hasta el 95%
93%
94%
95%
'''
# La batería tiene inicialmente una carga cualquiera, por ejemplo 92
bateria = 92

# Por siempre, voy cargando la batería
while True:
    # Sumo en 1 el valor de batería y lo muestro por pantalla
    bateria += 1
    print(f"{bateria}%")

    # Si la batería es igual o mayor a 95
    if bateria >= 95:
        # Rompo el bucle y termino
        break