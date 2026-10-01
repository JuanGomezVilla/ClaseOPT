# Soluciones - Ejercicios de repaso

1. Número positivo: pide un número al usuario e indica si es positivo.
    ```py
    numero = int(input("Número: "))

    if numero > 0:
        print("Número positivo")
    ```
2. Número negativo: pide un número e indica si es negativo o no.
    ```py
    numero = int(input("Número: "))

    if numero < 0:
        print("El número es negativo")
    else:
        print("El número no es negativo")
    ```
3. Mayor de edad: pide la edad de una persona. Indica si es mayor de edad o menor de edad.
    ```py
    edad = int(input("Edad: "))

    if edad >= 18:
        print("Mayor de edad")
    else:
        print("Menor de edad")
    ```
4. Número par: pide un número e indica si es par o impar.
    ```py
    numero = int(input("Número: "))

    if numero%2:
        print("Impar")
    else:
        print("Par")
    ```
5. Aprobado o suspenso: pide una nota. Si es 5 o más, muestra "Aprobado". En caso contrario, muestra "Suspenso".
    ```py
    nota = int(input("Nota: "))

    if nota >= 5:
        print("Aprobado")
    else:
        print("Suspenso")
    ```
6. Número cero: pide un número e indica si es positivo, negativo o cero.
    ```py
    numero = int(input("Número: "))

    if numero > 0:
        print("Positivo")
    elif numero == 0:
        print("Cero")
    else:
        print("Negativo")
    ```
7. Mayor de dos números: pide dos números e indica cuál de ellos es mayor.
    ```py
    numero1 = int(input("Número 1: "))
    numero2 = int(input("Número 2: "))

    if numero1 > numero2:
        print(f"{numero1} es mayor que {numero2}")
    elif numero1 < numero2:
        print(f"{numero2} es mayor que {numero1}")
    else:
        print("Ambos números dados son iguales")
    ```
8. ¿Son iguales? pide dos números e indica si son iguales o diferentes.
    ```py
    numero1 = int(input("Número 1: "))
    numero2 = int(input("Número 2: "))

    if numero1 == numero2:
        print("Los números son iguales")
    else:
        print("Los números son distintos")
    ```
9. Temperatura: pide una temperatura. Si es menor que 10, muestra "Hace frío". Si no, muestra "No hace frío".
    ```py
    temperatura = int(input("Temperatura: "))

    if temperatura < 10:
        print("Hace frío")
    else:
        print("No hace frío")
    ```
10. Contraseña sencilla: pide una contraseña. Si es "python123", muestra "Contraseña correcta". Si no, muestra "Contraseña incorrecta".
    ```py
    password = input("Contraseña: ")

    if password == "python123":
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta")
    ```
11. Número mayor que 100: pide un número e indica si es mayor que 100 o no.
    ```py
    numero = int(input("Número: "))

    if numero > 100:
        print("Número mayor que 100")
    else:
        print("El número no es mayor que 100")
    ```
12. Edad para conducir: pide la edad. Si tiene 18 años o más, muestra "Puedes conducir". Si no, muestra "No puedes conducir".
    ```py
    edad = int(input("Edad: "))

    if edad >= 18:
        print("Puedes conducir")
    else:
        print("No puedes conducir")
    ```
13. Precio con descuento: pide el precio de un producto. Si cuesta más de 50 €, muestra "Tiene descuento". Si no, muestra "No tiene descuento".
    ```py
    precio = int(input("Precio: "))

    if precio > 50:
        print("Tiene descuento")
    else:
        print("No tiene descuento")
    ```
14. Nota con tres resultados: pide una nota. Si es menor que 5, muestra "Suspenso". Si está entre 5 y 6, muestra "Aprobado". Si es mayor de 6, muestra "Buena nota".
    ```py
    nota = int(input("Nota: "))

    if nota < 5:
        print("Suspenso")
    elif nota >= 5 and nota <= 6:
        print("Aprobado")
    else:
        print("Buena nota")
    ```
15. Temperatura con tres opciones: pide una temperatura. Menos de 10: "Frío". Entre 10 y 25: "Templado". Más de 25: "Calor".
    ```py
    temperatura = int(input("Temperatura: "))

    if temperatura < 10:
        print("Hace frío")
    elif temperatura >= 10 and temperatura <= 25:
        print("Templado")
    else:
        print("Calor")
    ```
16. Día de la semana: pide un número del 1 al 7. Muestra el día correspondiente. Por ejemplo, 1 → "Lunes" y 7 → "Domingo".
    ```py
    dia = int(input("Nº de día: "))

    if dia == 1:
        print("Lunes")
    elif dia == 2:
        print("Martes")
    elif dia == 3:
        print("Miércoles")
    elif dia == 4:
        print("Jueves")
    elif dia == 5:
        print("Viernes")
    elif dia == 6:
        print("Sábado")
    elif dia == 7:
        print("Domingo")
    else:
        print("Fuera de rango")
    ```
17. Mes: pide un número del 1 al 12 e indica el nombre del mes.
    ```py
    mes = int(input("Nº de mes: "))

    if mes == 1:
        print("Enero")
    elif mes == 2:
        print("Febrero")
    elif mes == 3:
        print("Marzo")
    elif mes == 4:
        print("Abril")
    elif mes == 5:
        print("Mayo")
    elif mes == 6:
        print("Junio")
    elif mes == 7:
        print("Julio")
    elif mes == 8:
        print("Agosto")
    elif mes == 9:
        print("Septiembre")
    elif mes == 10:
        print("Octubre")
    elif mes == 11:
        print("Noviembre")
    elif mes == 12:
        print("Diciembre")
    else:
        print("Fuera de rango")
    ```
18. Semáforo: pide un color ("rojo", "amarillo" o "verde") y muestra qué debe hacer una persona: parar, tener precaución o pasar.
    ```py
    semaforo = input("Semáforo [rojo|amarillo|verde]: ")

    if semaforo == "rojo":
        print("Parar")
    elif semaforo == "amarillo":
        print("Precaución")
    elif semaforo == "verde":
        print("Pasar")
    else:
        print("Opción desconocida")
    ```
19. Clasificar números: pide un número. Indica si es menor que 0, igual a 0 o mayor que 0.
    ```py
    numero = int(input("Número: "))

    if numero < 0:
        print("Menor que 0")
    elif numero == 0:
        print("0")
    elif numero > 0:
        print("Mayor que 0")
    ```
20. Número dentro de un rango: pide un número. Indica si está entre 1 y 10.
    ```py
    numero = int(input("Número: "))

    if numero >= 0 and numero <= 10:
        print("Está entre 0 y 10")
    else:
        print("Fuera de rango")
    ```
21. Número fuera de un rango: pide un número. Indica si está fuera del rango 1-100.
    ```py
    numero = int(input("Número: "))

    if numero >= 0 and numero <= 100:
        print("Está entre 0 y 100")
    else:
        print("Fuera de rango")
    ```
22. Acceso a una atracción: pide la altura en centímetros. Si mide 120 cm o más, puede subir. Si mide menos, no puede.
    ```py
    altura = int(input("Altura: "))

    if altura >= 120:
        print("Puede pasar")
    else:
        print("No puede pasar")
    ```
23. Entrada al cine: pide la edad. Menores de 12 años pagan 5 €. El resto paga 8 €.
    ```py
    edad = int(input("Edad: "))

    if edad < 12:
        print("Precio: 5€")
    else:
        print("Precio: 8€")
    ```
24. Número divisible entre 5: pide un número e indica si es divisible entre 5 (resto cero)
    ```py
    numero = int(input("Número: "))

    if numero%5 == 0:
        print("Divisible por 5")
    else:
        print("No es divisible por 5")
    ```
25. Número divisible entre 2 y 3: pide un número e indica si es divisible entre 2, entre 3 o entre ninguno de los dos.
    ```py
    numero = int(input("Número: "))

    if numero%2 == 0:
        print("Divisible por 2")
    elif numero%3 == 0:
        print("Divisible por 3")
    else:
        print("No es divisible por 2 ni 3")
    ```
26. Hora del día: pide una hora entre 0 y 23. Si es de 6 a 11, muestra "Mañana". De 12 a 19, "Tarde". En otro caso, "Noche".
    ```py
    hora = int(input("Hora: "))

    if hora > 6 and hora < 12:
        print("Mañana")
    elif hora >= 12 and hora <= 19:
        print("Tarde")
    else:
        print("Noche")
    ```
27. Saludo según la hora: pide una hora. Si es antes de las 12, muestra "Buenos días". Si es entre las 12 y las 20, "Buenas tardes". Si no, "Buenas noches".
    ```py
    hora = int(input("Hora: "))

    if hora < 12:
        print("Buenos días")
    elif hora >= 12 and hora <= 20:
        print("Buenas tardes")
    else:
        print("Buenas noches")
    ```
28. Calculadora sencilla: pide dos números y una operación (+, -, * o /). Según la operación introducida, realiza el cálculo.
    ```py
    numero1 = int(input("Número 1: "))
    numero2 = int(input("Número 2: "))
    operacion = input("Operación [+|-|*|/]: ")

    if operacion == "+":
        print(f"{numero1} + {numero2} = {numero1 + numero2}")
    elif operacion == "-":
        print(f"{numero1} - {numero2} = {numero1 +-numero2}")
    elif operacion == "*":
        print(f"{numero1} * {numero2} = {numero1 * numero2}")
    elif operacion == "/":
        print(f"{numero1} / {numero2} = {numero1 / numero2}")
    else:
        print("Operación no reconocida")
    ```
29. ¿Puede votar?: pide la edad. Si tiene 18 o más, muestra "Puedes votar". Si no, muestra "Todavía no puedes votar".
    ```py
    edad = int(input("Edad: "))

    if edad >= 18:
        print("Puedes votar")
    else:
        print("Todavía no puedes votar")
    ```
30. Número secreto: guarda un número secreto, por ejemplo 7. Pide al usuario que introduzca un número. Indica si ha acertado o no.
    ```py
    numero_secreto = 7
    numero = int(input("Número: "))

    if numero_secreto == numero:
        print("Número correcto")
    else:
        print("Fallo")
    ```