# Ejercicios de funciones

1. Crea una función llamada `saludar()` que muestra por pantalla *Hola*. Ejemplo:
    ```python
    saludar() # Hola
    ```
    **Solución:**
    ```python
    def saludar():
        print("Hola")
    ```
2. Crea una función llamada `mostrar_nombre(nombre)` que reciba un nombre como parámetro y muestre un saludo personalizado. Ejemplo:
    ```python
    mostrar_nombre("Fulano") # Hola, Fulano
    mostrar_nombre("Mengano") # Hola, Mengano
    mostrar_nombre("Zutano") # Hola, Zutano
    ```
    **Solución:**
    ```python
    def mostrar_nombre(nombre):
        print(f"Hola, {nombre}")
    ```
3. Crea una función llamada `mostrar_numero(numero)` que reciba un número y lo muestre por pantalla. Ejemplo:
    ```python
    mostrar_numero(4) # 4
    mostrar_numero(3) # 3
    mostrar_numero(6) # 6
    ```
    **Solución:**
    ```python
    def mostrar_numero(numero):
        print(numero)
    ```
4. Crea una función llamada `dibujar_linea()` que muestre 10 guiones. Ejemplo:
    ```python
    dibujar_linea() # ----------
    ```
    **Solución:**
    ```python
    def dibujar_linea():
        print("----------") # print("-" * 10)
    ```
5. Crea una función `sumar(a, b)` que reciba dos números y devuelva su suma. Ejemplo
    ```python
    resultado = sumar(4, 6)
    print(resultado) # 10
    ```
    **Solución:**
    ```python
    def sumar(a, b):
        suma = a + b
        return suma
    ```
6. Crea una función `restar(a, b)` que devuelva la resta del primer número menos el segundo. No crees variables dentro de la función. Ejemplo
    ```python
    resultado = restar(10, 4)
    print(resultado) # 6
    ```
    **Solución:**
    ```python
    def restar(a, b):
        return a - b
    ```
7. Crea una función `multiplicar(a, b)` que devuelva el producto de dos números. De nuevo, no crees variables dentro de la función. Ejemplo
    ```python
    print(multiplicar(3, 9)) # 27
    ```
    **Solución:**
    ```python
    def multiplicar(a, b):
        return a * b
    ```
8. Crea una función `cuadrado(numero)` que devuelva el cuadrado de un número (elevado a 2 o multiplicado por sí mismo). Ejemplo:
    ```python
    print(cuadrado(5)) # 25
    ```
    **Solución:**
    ```python
    def cuadrado(numero):
        return numero ** 2 # numero * numero
    ```
9. Crea una función `doble(numero)` que devuelva el doble del número recibido. Ejemplo:
    ```python
    print(doble(4)) # 8
    ```
    **Solución:**
    ```python
    def doble(numero):
        return numero * 2 # numero + numero
    ```
10. Crea una función `mitad(numero)` que devuelva la mitad de un número. Ejemplo:
    ```python
    print(mitad(6)) # 3
    ```
    **Solución:**
    ```python
    def mitad(numero):
        return numero / 2
    ```