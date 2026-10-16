# Parte 1. Bucles finitos
1. Contar del 1 al 10
    ```python
    # Para números entre el 1 (incluido) y el 11 (sin incluir)
    for i in range(1, 11):
        # Muestra el valor de i (iterador)
        print(i)
    ```
    ```python
    # Alternativamente, de 0 (incluido) al 10 (sin incluir)
    for i in range(10):
        # Pero a la hora de imprimir, le sumo 1
        print(i + 1)
    ```
2. Mostrar los números pares del 2 al 20
    ```python
    # Empieza desde el 2 incluido hasta el 21 sin incluir, avanzando de 2 en 2
    for i in range(2, 21, 2):
        # Muestra el valor del iterador
        print(i)
    ```
3. Sumar los números del 1 al 100
    ```python
    # La suma inicialmente es 0
    suma = 0

    # Para números entre el 1 (incluido) y el 101 (sin incluir)
    for i in range(1, 101):
        # Suma el iterador al total
        suma += i

    # Imprime el total
    print(suma)
    ```
4. Mostrar la tabla de multiplicar de un número solicitado al usuario
    ```python
    # Pide un número al usuario
    numero = int(input("Número: "))

    # Itera del 1 al 10, ambos incluidos, sin contar el 11
    for i in range(1, 11):
        # Muestra la tabla con salida formateada
        print(f"{i} x {numero} = {i * numero}")
    ```
5. Recorrer una lista de alumnos
    ```python
    alumnos = ["Ana", "Luis", "Marta", "Pablo"]

    # Para cada alumno de los alumnos
    for alumno in alumnos:
        # Imprime el nombre del alumno
        print(alumno)
    ```
6. Mostrar las letras de un nombre
    ```python
    nombre = "Mengano"

    # Para cada letra del nombre
    for letra in nombre:
        # Imprime la letra
        print(letra)
    ```
7. Recorrer una lista utilizando `range()` y `len()`
    ```python
    alumnos = ["Ana", "Luis", "Marta"]

    # Tantas veces como alumnos existan
    for i in range(len(alumnos)):
        # Imprime el valor del iterador, desde 0 hasta N-1, donde N = nº de alumnos
        print(alumnos[i])
    ```
8. Mostrar una lista numerada de marcas de coches
    ```python
    marcas = ["Seat", "Ford", "Cupra", "Audi"]

    # Tantas veces como marcas existan
    for i in range(len(marcas)):
        # Incrementa en 1 la iteración y muestra el valor en la posición según el iterador
        print(f"{i+1}. {marcas[i]}")
    ```
    ```python
    marcas = ["Seat", "Ford", "Cupra", "Audi"]

    # Contador iniciado a 1
    contador = 1

    # Para cada marca de las marcas
    for marca in marcas:
        # Muestra cada marca e incrementa el contador
        print(f"{contador}. {marca}")
        contador += 1
    ```

9. Detener un bucle cuando encontremos un nombre, por ejemplo, *Marta*
    ```python
    alumnos = ["Ana", "Luis", "Marta", "Pablo"]

    # Para cada alumno de los alumnos
    for alumno in alumnos:
        # Imprime el nombre del alumno
        print(alumno)

        # Si el nombre es Marta, rompe el bucle, y no imprime más
        if alumno == "Marta":
            break
    ```
    Una forma alternativa de este ejercicio, si queremos ocultar el nombre en lugar de romper el bucle (para imprimir los siguientes), es utilizar la palabra clave `continue`:
    ```python
    alumnos = ["Ana", "Luis", "Marta", "Pablo"]

    # Para cada alumno de los alumnos
    for alumno in alumnos:
        # Si el nombre es Marta
        if alumno == "Marta":
            # Continua a la siguiente iteración saltando el código a continuación
            continue
        
        # Imprime el nombre del alumno
        print(alumno)
    ```
    > No confundir con *pass*, donde prácticamente, no hace nada
10. Contar cuántas veces aparece la letra *a* en una palabra
    ```python
    palabra = "cargador"
    contador = 0

    # Para cada letra de las palabras
    for letra in palabra:
        # Si la letra en esa iteración es la "a"
        if letra == "a":
            # Incrementa en 1 el contador
            contador += 1

    print(contador)
    ```
11. Sumar los números de una lista
    ```python
    numeros = [4, 7, 2, 9]

    # Variable con el total a 0
    suma = 0

    # Para cada numero de los números
    for numero in numeros:
        # Suma el número a la suma total
        suma += numero

    # Muestra el resultado
    print(suma)
    ```
12. Encontrar el número mayor de una lista
    ```python
    numeros = [8, 3, 15, 6, 11]

    # El mayor número es por defecto, el primero de todos
    mayor = numeros[0]

    # Para cada número de los números
    for numero in numeros:
        # Si el número actual es superior al mayor, lo actualiza
        if numero > mayor:
            # Guarda el número
            mayor = numero

    # Muestra el número mayor
    print(mayor)
    ```
13. Mostrar solamente determinadas marcas
    ```python
    marcas = ["Seat", "Ford", "Cupra", "Audi"]

    # Para cada marca de las marcas
    for marca in marcas:
        # Muestra solo "Seat" y "Cupra"
        if marca == "Seat" or marca == "Cupra":
            # Imprime la marca
            print(marca)
    ```
14. Calcular la media de varias notas
    ```python
    notas = [7, 8, 6, 9]

    # Variables de cálculo
    media = 0
    suma = 0

    # Para cada nota de las notas
    for nota in notas:
        # Aplica la suma
        suma += nota

    # Obtiene la media al dividir (suma total / nº de notas)
    media = suma / len(notas)

    # Imprime el resultado
    print(media)
    ```
15. Contar cuántas notas están aprobadas
    ```python
    notas = [4, 7, 5, 3, 9, 6]

    # Definir un contador
    contador = 0

    # Para cada nota de las notas
    for nota in notas:
        # Si la nota es igual o superior a 5, incremeta el contador
        if nota >= 5:
            contador += 1

    # Muestra el resultado
    print(f"Asignaturas aprobadas: {contador}")
    ```

<br>

# Parte 2. Bucles infinitos
1. Cargar una batería hasta llegar al 100
    ```python
    # Valor de la batería inicialmente
    bateria = 85

    # Siempre que la batería sea menor que 100
    while bateria < 100:
        # Incrementa en 1 la batería y muestra el valor
        bateria += 1
        print(bateria)
    ```
    > El *print* va después del incremento, para mostrar el resultado actualizado en esa iteración
2. Incrementar una nota hasta llegar al 10
    ```python
    # Valor inicial de la nota
    nota = 4

    # Siempre que la nota sea inferior a 10
    while nota < 10:
        # Incrementa la nota en 1 y muestra el valor
        nota += 1
        print(nota)
    ```
3. Pedir una contraseña hasta acertar
    ```python
    # Contraseña original para adivinar
    password = "hola"

    # Por siempre
    while True:
        # Pide una contraseña al usuario
        user_password = input("Contraseña: ")

        # Si la contraseña del usuario es igual a la original, rompe el bucle
        if user_password == password:
            break
        else:
            # En caso contrario, muestra un mensaje de contraseña incorrecta
            print("Contraseña incorrecta, inténtalo de nuevo...")

    # Imprime un mensaje de fin de programa
    print("Fin del programa")
    ```
4. Adivinar un número secreto
    ```python
    # Número secreto
    numero_secreto = 5

    # Por siempre
    while True:
        # Pide un número al usuario y lo convierte a entero
        numero = int(input("Número: "))

        # Si el número de usuario es igual al secreto, rompe el bucle
        if numero == numero_secreto:
            break
        else:
            # En caso contrario, se lo dice al usuario
            print("Número incorrecto")

    # Fin del programa
    print("Fin del programa")
    ```
5. Contar hacia atrás desde 10
    ```python
    # Contador iniciado a 10
    contador = 10

    # Siempre que el número sea mayor o igual a 1
    while contador >= 1:
        # Muestro su valor y le resto 1
        print(contador)
        contador -= 1
    
    # Finaliza con un mensaje
    print("Fin de la cuenta")
    ```
6. Sumar números hasta que se introduzca un cero
    ```python
    # La suma inicialmente es 0
    suma = 0

    # Por siempre
    while True:
        # Pido al usuario un número
        numero = int(input("Número: "))

        # Si el número es 0, rompo el bucle
        if numero == 0:
            break

        # Sumo el valor
        suma += numero

    # Imprimo el resultado final
    print(f"Suma total: {suma}")
    ```
7. Pedir palabras hasta escribir `salir`
    ```python
    # Por siempre
    while True:
        # El usuario escribe una palabra
        palabra = input("Palabra: ")

        # Si la palabra es igual a "salir", rompe el bucle
        if palabra == "salir":
            break

        # Muestra la palabra
        print(f"Has escrito {palabra}")

    # Mensaje de fin
    print("Programa finalizado")
    ```
8. Repetir una pregunta hasta recibir una respuesta válida
    ```python
    # La respuesta inicialmente es un valor nulo
    respuesta = None

    # Siempre que la respuesta sea distinta de "si" o "no"
    while respuesta != "si" and respuesta != "no":
        # Pide al usuario una respuesta
        respuesta = input("¿Quieres continuar? (si/no): ")

    # Mensaje de fin
    print("Fin del programa")
    ```
9. Mostrar los números pares hasta un límite definido por el usuario en consola
    ```python
    # El usuario escribe el límite. El número inicialmente es el posible par, el 2
    limite = int(input("Límite: "))
    numero = 2

    # Siempre que el número sea menor o igual al límite
    while numero <= limite:
        # Imprime el número y le incrementa 2
        print(numero)
        numero += 2
    ```
10. Multiplicar un número por dos hasta llegar a 100
    ```python
    # Número definido por el usuario
    numero = int(input("Número: "))

    # Siempre que el número sea menor o igual a 100
    while numero <= 100:
        # Imprime el número y lo multiplica por 2
        print(numero)
        numero *= 2
    ```
11. Permitir un máximo de tres intentos de contraseña
    ```python
    # VARIABLES
    password = "hola"           # Contraseña
    intentos = 0                # Intentos realizados
    acceso_concedido = False    # Trigger que se activa si acierta

    # Siempre que los intentos sean inferiores a 3 y el acceso no se haya activado
    while intentos < 3 and acceso_concedido == False:
        # Pide una contraseña al usuario
        user_password = input("Contraseña: ")

        # Comprueba si es correcto
        if user_password == password:
            # Al ser correcto, activa el trigger, que finaliza el bucle con la comprobación
            acceso_concedido = True
        else:
            # Aumenta el número de intentos y notifica al usuario
            intentos += 1
            print(f"Contraseña incorrecta, intentos realizados: {intentos}")


    # Comprueba si se ha activado el trigger
    if acceso_concedido:
        print("Bienvenido")
    else:
        print("Has agotado el número de intentos")
    ```
12. Contar números hasta introducir uno negativo
    ```python
    # Contador a 0
    contador = 0

    # Por siempre, pido números al usuario
    while True:
        # El usuario escribe un número
        numero = int(input("Número: "))

        # Si el número es inferior a 0, rompe el bucle
        if numero < 0:
            break

        # Incrementa el contador
        contador += 1

    # Muestra la cantidad de números no negativos escritos
    print(f"Números no negativos escritos: {contador}")
    ```
13. Guardar nombres en una lista hasta escribir `fin`
    ```python
    # Lista de nombres inicialmente vacía
    nombres = []

    # Por siempre
    while True:
        # Pide un nombre al usuario
        nombre = input("Nombre: ")

        # Si el nombre es "fin", rompe el bucle
        if nombre == "fin":
            break

        # Añade el nombre a la lista
        nombres.append(nombre)

    # Muestra los nombres escritos
    print("\nNombres escritos:")
    for nombre in nombres:
        print(f"   - {nombre}")
    ```
14. Crear un menú que se repita hasta elegir salir
    ```python
    # Por siempre
    while True:
        # Mostrar un menú
        print("1. Ver coches\n2. Crear coche\n3. Salir")

        # Pedir al usuario un valor
        opcion = int(input("OPCIÓN: "))
        print() # Salto de línea adicional

        # Analizar cada situación según la opción
        if opcion == 1:
            print("Imprimiendo coches")
            
        elif opcion == 2:
            print("Creando un coche")

        elif opcion == 3:
            break # Rompe el bucle
        else:
            print("Opción no válida...")

        # Salto de línea adicional
        print()

    # Mensaje de finalización
    print("Fin del programa")
    ```
15. Sumar números hasta alcanzar al menos 50
    ```python
    # Suma inicialmente a 0
    suma = 0

    # Siempre que la suma sea inferior a 50
    while suma < 50:
        # Pide al usuario un número
        numero = int(input("Número: "))

        # Realiza la suma
        suma += numero

        # Imprime el valor actual
        print(f"Valor actual: {suma}")

    # Fin del programa
    print("Se ha alcanzado el 50, fin del programa")
    ```