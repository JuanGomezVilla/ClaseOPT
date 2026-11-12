# Por siempre
while True:
    # Pido al usuario por un texto, una opción, un producto, lo que sea
    opcion = input("Producto: ")

    # Compruebo si el usuario ha escrito exit
    if opcion == "exit":
        break

    # Compruebo el nombre del producto

    # Si la opción es una camiseta, muestro su precio
    if opcion == "camiseta":
        print("Precio: 10€")

    # Si la opción es zapatos, muestro su precio
    elif opcion == "zapatos":
        print("Precio: 15€")

    # Si la opción es sudadera, muestro su precio
    elif opcion == "sudadera":
        print("Precio: 20€")

    # Si no es exit, ni ninguna opción cualquiera
    else:
        # Es un producto no encontrado
        print("Producto no encontrado")

    