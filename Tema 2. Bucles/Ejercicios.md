1. Pedir números al usuario por consola hasta que ponga uno negativo
    - Esquema mental:
        ```
        Por siempre
            Pido un número

            Compruebo si es negativo
                En caso afirmativo, rompo el bucle
        ```
    - Solución:
        ```py
        while True:
            numero = int(input("Número: "))

            if numero < 0:
                break
        ```
2. Un programa pide una contraseña y finaliza cuando se acierta
    - Esquema mental:
        ```
        Por siempre
            Pido contraseña

            ¿La contraseña es "hola"?
                Si es correcto, rompo el bucle
            
            Si falla, contraseña incorrecta

        Bienvenido
        ```
    - Solución:
        ```py
        password = "hola"

        while True:
            user_password = input("CONTRASEÑA: ")

            if user_password == password:
                break

            print("Contraseña incorrecta, inténtalo de nuevo...")

        print("Bienvenido")
        ```
3. Imprimir números del 1 al 10:
    ```py
    for i in range(1, 11):
        print(i)
    ```
4. Imprimir los números pares del 1 al 25, utilizando un `if`:
    ```py
    for i in range(1, 25):
        if i%2 == 0:
            print(i)
    ```
5. Pedir al usuario una palabra y contar el número de letras con un bucle finito, sin utilizar `len()`:
    ```py
    palabra = input("Palabra: ")
    contador = 0

    for letra in palabra:
        contador += 1

    print(contador)
    ```
6. Crea una lista con tus notas y calcula la media:
    ```py
    notas = [5, 6, 7, 8]
    suma = 0
    numero_notas = 0

    for nota in notas:
        suma += nota
        numero_notas += 1

    media = suma / numero_notas

    print(media)
    ```
    Alternativa:
    ```py
    notas = [5, 6, 7, 8]

    media = sum(notas) / len(notas)

    print(media)
    ```
7. Crea una lista de nombres e imprimelos con enumeración
    ```py
    nombres = ["Fulano", "Mengano", "Zutano", "Perantano"]

    contador = 1

    for nombre in nombres:
        print(f"{contador}. {nombre}")
        contador += 1
    ```