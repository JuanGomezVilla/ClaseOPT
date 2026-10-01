```py
# 1. Pide un número e indica si es positivo o negativo
numero = int(input("Número: "))

if numero > 0:
    print("Positivo")
else:
    print("Negativo")
```

```py
# 2. Pide un número y determina si es par o impar
numero = int(input("Número: "))

if numero%2:
    print("Impar")
else:
    print("Par")
```

```py
# 3. Aprobado o suspenso en base a una nota escrita por el usuario
nota = int(input("Nota: "))

if nota < 5:
    print("Suspenso")
else:
    print("Aprobado")
```

```py
edad = int(input("EDAD: "))

if edad > 18:
    print("Es mayor de edad")
elif edad == 18:
    print("Tiene 18 exactamente")
else:
    print("Es menor de edad")
```