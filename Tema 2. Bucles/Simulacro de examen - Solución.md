# Simulacro de examen - Solución

1. **(1 punto)** Dada la siguiente lista de nombres, imprímelos por pantalla con enumeración
    - **Base:**
        ```python
        nombres = ["Mengano", "Fulano", "Zutano"]
        ```
    - **Resultado de ejemplo:**
        ```
        1. Mengano
        2. Fulano
        3. Zutano
        ```
    - **Soluciones:**
        ```python
        nombres = ["Mengano", "Fulano", "Zutano"]
        
        # Contador inicial a 1
        contador = 1

        # Para cada nombre de los nombres
        for nombre in nombres:
            # Imprimir el contador con el nombre
            print(f"{contador}. {nombre}")

            # Incrementar en 1 el contador
            contador += 1
        ```
        ```python
        nombres = ["Mengano", "Fulano", "Zutano"]

        # Un iterador que se ejecutará en un rango 0-(nº de nombres, sin incluir)
        for i in range(len(nombres)):
            # Incrementa el iterador, pero esto solo afecta al imprimir, no posteriormente
            # Imprime el nombre según la posición del iterador
            print(f"{i+1}. {nombres[i]}")
        ```
2. **(1 punto)** Pedir al usuario números e ir sumándolos hasta que escriba el 0
    - **Base:**
        ```python
        
        ```
    - **Resultado de ejemplo:**
        ```
        NÚMERO: 1
        NÚMERO: 4
        NÚMERO: 10
        NÚMERO: 0
        15
        ```
    - **Solución:**
        ```python
        suma = 0

        # Por siempre
        while True:
            # Pido un número por consola
            numero = int(input("NÚMERO: "))

            # Si el número es 0, rompo el bucle
            if numero == 0:
                break

            # Sumo el número escrito
            suma += numero

        # Imprimo la suma resultante
        print(suma)
        ```
3. **(1 punto)** Mostrar los números pares del 2 al 10, ambos incluidos
    - **Base:**
        ```python
        
        ```
    - **Resultado de ejemplo:**
        ```
        2
        4
        6
        8
        10
        ```
    - **Solución:**
        ```python
        # Del 2 incluido, al 11 sin incluir, de 2 en 2
        for i in range(2, 11, 2):
            # Imprime el valor del iterador
            print(i)
        ```
4. **(1 punto)** Imprimir los valores de la siguiente lista y detener si aparece *silla*
    - **Base:**
        ```python
        elementos = ["mesa", "puerta", "ventana", "silla", "coche"]
        ```
    - **Resultado de ejemplo:**
        ```
        mesa
        puerta
        ventana
        ```
    - **Solución:**
        ```python
        elementos = ["mesa", "puerta", "ventana", "silla", "coche"]

        # Para cada elemento de los elementos
        for elemento in elementos:
            # Si el elemento es silla, rompo el bucle
            if elemento == "silla":
                break

            # Imprimo el elemento
            print(elemento)
        ```
5. **(1 punto)** Una batería tiene una carga del 95%, cárgala hasta que aparezca 100%. Ten en cuenta que la carga puede variar, no siempre será 95%.
    - **Base:**
        ```python
        bateria = 95
        ```
    - **Resultado de ejemplo:**
        ```
        96%
        97%
        98%
        99%
        100%
        ```
    - **Solución:**
        ```python
        bateria = 95

        # Siempre que la batería sea menor a 100
        while bateria < 100:
            # Incrementa en 1 la batería
            bateria += 1

            # Muestra su estado actual con un porcentaje
            print(f"{bateria}%")
        ```
        > La suma no puede ir después del *print*, porque no se mostraría el cambio hasta el próximo ciclo

6. **(5 puntos)** Realiza el siguiente ejercicio por partes
    1. **(1 punto)** Define una lista llamada *marcas* que contenga 5 marcas
        ```python
        marcas = ["Fiat", "Seat", "Ferrari", "Audi", "BMW"]   # <--
        ```
    2. **(1 punto)** El concesionario quiere que imprimas por pantalla cada marca de coche, con un guión previo, el resultado debe verse así:
        ```
        - Fiat
        - Seat
        - Ferrari
        - Audi
        - BMW
        ```
        **Solución:**
        ```python
        marcas = ["Fiat", "Seat", "Ferrari", "Audi", "BMW"]

        for marca in marcas:        # <--
            print(f"- {marca}")     # <--
        ```
    3. **(1 punto)** Este listado funcionará como un menú. El usuario tendrá que escribir una marca por pantalla y luego volverá a mostrar el menú, por siempre. Si escribe *exit*, el menú termina, y el programa finaliza:
        ```
        - Fiat
        - Seat
        - Ferrari
        - Audi
        - BMW
        OPCIÓN: exit
        ```
        **Solución:**
        ```python
        marcas = ["Fiat", "Seat", "Ferrari", "Audi", "BMW"]

        while True:                     # <--
            for marca in marcas:
                print(f"- {marca}")

            opcion = input("OPCIÓN: ")  # <--

            if opcion == "exit":        # <--
                break                   # <--
        ```
    4. **(1 punto)** Si no escribe *exit* pero tampoco ninguna de las marcas existentes, muestra el mensaje *Marca no encontrada*, y muestra de nuevo el menú, teniendo en cuenta los saltos de línea:
        ```
        - Fiat
        - Seat
        - Ferrari
        - Audi
        - BMW
        OPCIÓN: perro

        Marca no encontrada

        - Fiat
        - Seat
        - Ferrari
        - Audi
        - BMW
        ```
        **Solución:**
        ```python
        marcas = ["Fiat", "Seat", "Ferrari", "Audi", "BMW"]

        while True:
            for marca in marcas:
                print(f"- {marca}")

            opcion = input("OPCIÓN: ")

            if opcion == "exit":
                break
            elif opcion not in marcas:              # <--
                print("\nMarca no encontrada\n")    # <--
        ```
    5. **(1 punto)** Por último, si no sucede ninguno de los casos anteriores (*exit* o marca inválida), quiere decir que escribe una marca que existe, muestra por pantalla el número de letras que tiene esa marca:
        ```python
        marcas = ["Fiat", "Seat", "Ferrari", "Audi", "BMW"]

        while True:
            for marca in marcas:
                print(f"- {marca}")

            opcion = input("OPCIÓN: ")

            if opcion == "exit":
                break
            elif opcion not in marcas:
                print("\nMarca no encontrada\n")
            else:                                                   # <--
                print(f"\n{opcion} tiene {len(opcion)} letras\n")   # <--
        ```

**Ejemplo de ejecución completa:**
```
- Fiat
- Seat
- Ferrari
- Audi
- BMW
OPCIÓN: Audi

Audi tiene 4 letras

- Fiat
- Seat
- Ferrari
- Audi
- BMW
OPCIÓN: Ferrari

Ferrari tiene 7 letras

- Fiat
- Seat
- Ferrari
- Audi
- BMW
OPCIÓN: perro

Marca no encontrada

- Fiat
- Seat
- Ferrari
- Audi
- BMW
OPCIÓN: exit
```