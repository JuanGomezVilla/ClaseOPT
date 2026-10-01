```py
# 1. Muestra los números del 10 al 1
numero = 10

while numero > 0:
    print(numero)
    numero -= 1
```

```py
# 2. Calcula y muestra la suma de todos los números del 1 al 10.
suma = 0
numero = 1

while numero <= 10:
    suma += numero
    numero += 1
    # print(f"Suma: {suma}, Numero:{numero}")

print(suma)
```

```py
# 3. Pide al usuario un número y muestra su tabla de multiplicar del 1 al 10
numero = int(input("Número: "))
i = 0


while i <= 10:
    print(f"{i} x {numero} = {i * numero}")
    i += 1
```