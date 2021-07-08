# Para los condicionales utilizo comparadores de decisión

'''
En los diagramas de flujo el condicional se expresa en rombo
utiliza comparadores de decisión (> < == !=) y operadores lógicos ( y(and) o(or) no(not))
'''

'''
Se necesita saber si el estudiante tuvo alto, medio o bajo rendimiento
[0;3) Rendimiento bajo
[3;4) Rendimiento medio
[4,5] Rendimiento alto
[] el numero va incluido
() No está inclído el número

'''

# if en secuencia 

def notas(nota1, nota2, nota3):
    promedio = round((nota1 + nota2 + nota3)/3,2) 
    maximo = max(nota1, nota2,nota3)
    minimo = min(nota1,nota2,nota3)
    if promedio >= 0 and promedio < 3:  # La condición se expresa con variables y operadores ( y siempre debo tener presente lo que voy a comparar)
        rendimiento = 'Bajo'
    if promedio >= 3 and  promedio < 4:
        rendimiento = 'Medio'
    if promedio >= 4 and promedio <= 5:
        rendimiento = 'Alto'
    

    return  f'El estudiante tiene una nota promedio de {promedio}, su mayor nota fue {maximo},  su menor nota fue {minimo}, y su rendimiento fue {rendimiento}' 


print(notas(3.5,4,4.6)) # con el print llamo la función y coloco los parámetros
print(notas(4,5,5))
print(notas(3,2,1))
print(notas(3,4, 3.6))

# Depuración y ejecución, permite hacer un seguimiento al programa 
# buscar como depura
# tambien se puede usar el else entre cada if
