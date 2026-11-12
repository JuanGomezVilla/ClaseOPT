'''
(1 punto) Pedir una palabra y comprueba si es palíndromo
PALABRA: kayak
Es palíndromo
'''
# Obtengo la palabra que el usuario escribe
palabra = input("PALABRA: ")

# Si la palabra es igual a la invertida
if palabra == palabra[::-1]:
    # Le digo al usuario que es un palíndromo
    print("Es palíndromo")
else:
    # En caso contrario, le digo que no es un palíndromo
    print("No es palíndromo")