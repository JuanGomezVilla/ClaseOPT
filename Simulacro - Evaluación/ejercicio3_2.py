'''
(1 punto) Una batería tiene una carga desconocida, cárgala hasta el 95%
93%
94%
95%
'''
# La batería inicialmente es 92, cualquier valor
bateria = 92

# Siempre que la batería sea inferior a 95, la voy cargando
while bateria < 95:
    # Incremento en 1 y muestro su valor
    bateria += 1
    print(f"{bateria}%")