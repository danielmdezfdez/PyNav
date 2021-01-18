import math

grados=0
minutos=0

def sexagesimal_console_print(valor):

    x = valor

    grados = int(valor)

    minutos = valor - int(valor)

    minutos = abs(minutos*60)

    solution = str(grados) + "º " + str(minutos) + "'"

    print(solution)

    return solution




sexagesimal_console_print(-28.5)