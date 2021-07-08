# Actividad Clase
'''
se necesita obtener el promedio de 3 notas parciales de la asignatura de ingles, muestres por pantalla el promedio de dichas calificaciones

construir el algoritmo, pero antes de eso identificar las entradas, el proceso necesario para calcular el promedio de notas y salida
'''

'''
ENTRADA
El valor de las notas obtenidas

PROCESO
Suma de las tres notas parciales dividida en 3

SALIDA
Promedio de las notas

'''

def promedio_sumar(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3)/3
    return promedio

nota1 = float(input("Digite la calificacion de la primer nota : "))
nota2 = float(input("Digite la calificacion de la segunda nota : "))
nota3 = float(input("Digite la calificacion de la tercer nota : "))
promedio = promedio_sumar(nota1, nota2, nota3)

print ("El promedio de las notas de ingles es : ",promedio)

'''
print ("El promedio de las notas de ingles es %.2f: ",promedio)
'''