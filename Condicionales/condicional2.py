'''
CONDICIONAL DOBLE

EStructura algoritmica de la condicional doble

Si <condicion> entonces
            Accion (es)
    si no
            Accion(es)
Fin si

Determiniar si un alumno aprueba o reprueba una asignatura,
aprueba si el promedio de tres calificaciones es mayor o igual a 3, en caso contrario reprueba

'''

calificacion1 = float(input("Digite calificación 1: "))
calificacion2 = float(input("Digite calificación 2: "))
calificacion3 = float(input("Digite calificación 3: "))

promedio = (calificacion1 + calificacion2 + calificacion3)/3

if promedio >= 3:
    print("El alumno aprobo")
else:
    print("El alumno reprobo")

print("El promedio del estudiante es: .%.2f "% promedio)

