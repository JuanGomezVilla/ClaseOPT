
```py
alumnos = ["Fulano", "Mengano", "Zutano"]

for alumno in alumnos:
    print(alumno)
```


```py
nombre = "Juan"

for letra in nombre:
    print(letra)
```

```py
alumnos = ["Fulano", "Mengano", "Zutano"]

print(len(alumnos))
```


```py
alumnos = ["Fulano", "Mengano", "Zutano"]

for i in range(0, 3, 1):
    print(alumnos[i])
```


```py
alumnos = ["Fulano", "Mengano", "Zutano"]

for i in range(len(alumnos)):
    print(alumnos[i])
```


```py
alumnos = ["Fulano", "Mengano", "Zutano"]

for alumno in alumnos:
    if alumno == "Mengano":
        break
    
    print(alumno)
```


marcas = ["Seat", "Ford", "Cupra", "Audi"]

if len(marcas) == 0:
    print("Todavía no hay marcas")
else:
    numero = 1

    for marca in marcas:
        print(f"{numero}. {marca}")
        numero += 1






marcas = ["Seat", "Ford", "Cupra", "Audi"]

if len(marcas) == 0:
    print("Todavía no hay marcas")
else:

    for i in range(len(marcas)):
        print(f"{i+1}. {marcas[i]}")
