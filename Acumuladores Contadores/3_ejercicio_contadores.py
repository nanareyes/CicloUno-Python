'''
Para ingresar al curso de Producción cinematográfica se realizó una prueba clasificatoria. 
Se tienen los resultados de dicho exámen por aspirante ( una nota comprendida entre 0.0 y 5.0.)

Se desea saber cuántos aspirantes aprobaron el examen, cuántos lo perdieron (nota menor que 3 0 ) y cuál fue el promedio de todo el grupo 
de aspirantes.
No sabemos cuántos aspirantes son, pero sabemos que cuando se quiera indicar que se finalizó el ingreso de notas se digitará un valor negativo.

'''
'''
Entrada : nota estudiante
Salida  : estudiantes que aprobaron y el promedio de todos ellos
Proceso :
i = 1
si nota estudiante >= 3.0 and
(i <= + 1) haga
nota estudiante += 1/n
   
i += 1

FIN

'''
nota = 0
suma = 0
aprobados = 0
perdidos = 0


while nota>= 0:
    nota = float(input("digite el valor de la nota: "))
    if (nota>= 0) and (nota <= 5):
        if nota >= 3:
            aprobados = aprobados+1
        else:
            perdidos = perdidos+1
    suma = suma + nota

total =aprobados + perdidos

def promedio_suma(n):
    promedio = round(suma/(total),2)
    return promedio

#respuesta


print(" El total de estudiantes que aprobaron el examen es de: ", (aprobados))
print (" El total de estudiantes que perdieron el examen es de: ", perdidos)
print("El promedio del total de las notas es de: ",promedio_suma(nota))
