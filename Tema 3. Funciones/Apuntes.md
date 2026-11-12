# Tema 3. Funciones

En programación, una función es un bloque de código que realiza una tarea específica y al que puedes llamar cuando lo necesites, sin tener que escribir el mismo código una y otra vez. Por ejemplo, si quiero crear un personaje en una determinada coordenada *(x, y)* de un mapa tres veces y esto requiere de varias líneas de código, puedo crear una función que, con pasarle unas coordenadas, lo ubica en el mapa, sin necesidad de repetir el fragmento:
```python
set_in_map(5, 4)
set_in_map(2, 1)
set_in_map(9, 3)
```

Puede decirse también que una función es un fragmento de código reducido a una línea (`saludar() = 10 líneas de código`). Esto nos permite ejecutar varias veces dicho fragmento sin necesidad de reescribirlo entero. En Python, para crear una función utilizamos la palabra reservada `def` y después el nombre de la función, seguido de los paréntesis, por ejemplo: `saludar()`. En el interior de esos paréntesis pueden ir parámetros, que lo veremos más adelante.
```python
def saludar():
    print("Hola")

saludar()
```

La función `imprimir()` muestra un saludo cada vez que es ejecutada:
```python
def imprimir():
    print("Hola")


imprimir()
imprimir()
imprimir()
```

Los argumentos son variables que se pasan a la función, y que cambian el valor con el que se trabaja en el interior:
```python
def imprimir(texto):
    print(texto)


imprimir("Hola")
imprimir("Juan")
imprimir("Adios")
```

Una función, metafóricamente, es como una caja. Por un extremo de la caja entra el valor, se procesa en el interior de la caja (la función) y pueden suceder dos casos:
- Que no pase nada
- Que por el extremo de la caja salga otro valor

Para estos dos ejemplos, no sucede nada. *Vale, sí*. Se imprime el resultado, pero no *sale fuera de la función*:
```python
def raiz_cuadrada(numero):
    raiz = numero ** 0.5
    print(raiz)


raiz_cuadrada(49)
raiz_cuadrada(100)
raiz_cuadrada(64)
```
```python
def sumar(numero1, numero2):
    suma = numero1 + numero2
    print(suma)


sumar(3, 4)
sumar(1, 8)
sumar(9, 3)
```

¿Cuál es la alternativa? Que un valor salga por el extremo de la caja, a esto se le conoce como devolución, aunque tiene muchas más acepciones.

Vamos a suponer el siguiente caso:
```python
def raiz_cuadrada(numero):
    resultado = numero ** 0.5
    print(resultado)

raiz_cuadrada(25)
raiz_cuadrada(64)
```

Hasta ahora, esta función imprime por pantalla el resultado, por medio del `print()`. Pero supongamos que ese valor, en lugar de imprimirlo, lo quiero guardar en una variable. Es decir, algo similar a esto:
```python
resultado1 = raiz_cuadrada(25)
resultado2 = raiz_cuadrada(64)
```

Por defecto, la última acción de la función es un `print()` pero esto no te permite asignar valores a las variables externas. Utilizamos `return`:
```python
def raiz_cuadrada(numero):
    resultado = numero ** 0.5
    return resultado

resultado1 = raiz_cuadrada(25)
resultado2 = raiz_cuadrada(64)
```

La instrucción `return` permite que una función devuelva un valor al lugar desde el que ha sido llamada. Ese valor puede almacenarse en una variable, utilizarse en una operación o emplearse directamente en otra parte del programa.