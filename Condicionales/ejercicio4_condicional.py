"""
Un operario registra la producción de muebles de oficina que logra de lunes a sábado. Elaborar un algoritmo que nos diga si el operario recibe incentivos o no, sabiendo
que el promedio de produccion mínima es de 20 iunidades a la semana. 
También debe imprimir la producción semanal de muebles

"""

print("\n")


def promedio_produccion(semana1, semana2, semana3, semana4):
    promedio = round(semana1 + semana2 + semana3 + semana4) / 4
    return promedio


semana1 = int(input("Digite la produccion de la semana1: "))
semana2 = int(input("Digite la produccion de la semana2: "))
semana3 = int(input("Digite la produccion de la semana3: "))
semana4 = int(input("Digite la produccion de la semana4: "))

promedio = promedio_produccion(semana1, semana2, semana3, semana4)
print("\n")
if promedio >= 20:
    print("Recibe incentivo")
else:
    print("No recibe incentivo")

print("\n")
print("El promedio de produccion del empleado es: %.2f" % promedio)
print("\n")
