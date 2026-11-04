while True:

    opcion = input("Resultado: ")

    if opcion == "exit":
        break

    resultado_equipo_1 = int(opcion[0])
    resultado_equipo_2 = int(opcion[2])

    if resultado_equipo_1 < resultado_equipo_2:
        print("Ha ganado el equipo 2")
    elif resultado_equipo_1 > resultado_equipo_2:
        print("Ha ganado el equipo 1")
    else:
        print("Empate")