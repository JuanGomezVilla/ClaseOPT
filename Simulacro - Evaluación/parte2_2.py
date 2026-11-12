'''
50€
-20%

descuento = precio_base * 30/100
          = 50 * 20/100 = 1000/100 = 10€

precio_tras_el_descuento = precio_base - descuento
                         = 50 - 10 = 40€
'''

def calcular_precio(precio:int, porcentaje_descuento:int):
    # Calcular el valor del descuento
    descuento = precio * (porcentaje_descuento/100)

    # Calculo el precio real = precio menos el descuento
    precio_real = precio - descuento

    # Devolver el precio real
    return precio_real


# Obtengo el valor y lo guardo en una variable
precio_tras_el_descuento = calcular_precio(37, 12)

# Muestro el valor de esa variable
print(precio_tras_el_descuento)