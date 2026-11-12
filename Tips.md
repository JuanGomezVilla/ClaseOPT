# Tips

<br>

## Tip 1 - Concatenar texto
El esquema siempre es el mismo:
```py
print(f"")
```

El texto que va en el interior a concatenar va entre llaves (`{...}`)
```py
print(f"Tienes {edad} años")
print(f"Su nombre es {nombre}")
```



<br>

## Tip 2 - Detectar cuando el usuario tiene que escribir
Si veo la palabra *pedir*:
1. Tiene que haber un `input()`
2. Busco el texto del resultado
3. Ese texto lo paso al `input` (por ejemplo, *EDAD:*):
    ```py
    input("EDAD: ")
    ```
4. Me pregunto el tipo de valor que estoy pidiendo:
    - *texto*, *palabra*: dejo el `input` tal cual
    - *número*, *edad*: convierto el `input` a entero:
        ```py
        int(input("EDAD: "))
        ```
5. El valor que me devuelve el `input` o convertirlo a `int` lo guardo en una variable:
    ```py
    edad = int(input("EDAD: "))
    ```



<br>

## Tip 3 - Estructura del bucle for
```py
for <variable> in <rango de valores>:
    codigo a ejecutar cada vez
```

Valor de `<variable>`:
- `i`: iterador, y se utiliza con números
- `nombre cualquier`: cuando es una lista de valores



<br>

## Tip 4 - Invertir una palabra
Utilizamos el siguiente comando:
```py
<variable>[::-1]
```

Por ejemplo:
```py
nombre[::-1]
palabra[::-1]
```



<br>

## Tip 5 - Controlar errores
Se utiliza la estructura `try-except`:
```py
try:
    # Código a intentar ejecutar
    # Generalmente, todo el código, pero no siempre
except:
    # Código a ejecutar si se desecandena un error
```



<br>

## Tip 6 - Cómo definir una función
1. Utilizar `def`:
    ```py
    def ...
    ```
2. Establecer un nombre de la función:
    ```py
    def calcular_precio
    ```
3. Añadir paréntesis, siempre:
    ```py
    def calcular_precio()
    ```
4. Añadir los dos *puntitos*:
    ```py
    def calcular_precio():
    ```
5. El contenido que va dentro de la función va tabulado
6. Añadir los parámetros dentro de los paréntesis:
    ```py
    def calcular_precio(precio, porcentaje):
    ```
7. Definir el tipo de parámetro:
    ```py
    def calcular_precio(precio:int, porcentaje:int):
    ```



<br>

## Tip 7 - Detectar un while
Si en el enunciado aparece la palabra clave *por siempre*, es:
```py
while True:
    ...
```



<br>

## Tip 8 - Calcular longitudes
- Utilizando `len()`:
    ```py
    palabra = "Fulano"
    print(len(nombre))
    ```
- Un bucle `for`:
    ```py
    palabra = "Fulano"

    cantidad = 0
    for letra in palabra:
        cantidad += 1
    
    print(cantidad)
    ```
- Utilizando `len()` combinado con un `for`:
    ```py
    palabra = "Fulano"

    cantidad = 0
    for i in range(len(palabra)):
        cantidad += 1
    
    print(cantidad)
    ```