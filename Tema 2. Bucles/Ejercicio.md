Elige un número aleatorio del 1 al 100. El usuario escribe un número y dice *menor* o *mayor*, de modo que va acotando para adivinarlo. Instrucciones:

- Una vez finalizado, muestra el siguiente mensaje:
    ```
    El número es <numero_aleatorio>. Intentos: <intentos>
    ```
- **Ejemplo de ejecución:**
    ```
    NÚMERO: 50
    Menor

    NÚMERO: 25
    Mayor

    NÚMERO: 34
    Mayor

    NÚMERO: 40
    Mayor

    NÚMERO: 45
    Menor

    NÚMERO: 43
    El número es 43. Intentos: 6
    ```
- **Código de inicio:**
    ```python
    import random

    numero_aleatorio = random.randint(0, 100)
    ```