# Calcular las notas de un estudiante, promedio, nota máxima y nota mínima

# def -> palabra reservada de python que significa definir

def notas(nota1, nota2, nota3):
    # Identación significa que todo lo que va debajo pertenece a la columna de acuerdo con la ubicación
    promedio = round((nota1 + nota2 + nota3)/3,2) # Primero se hace lo que hay en paréntesis, para que el resultado no arroje muchos decimales utilizo el round
    maximo = max(nota1, nota2,nota3)
    minimo = min(nota1,nota2,nota3)
# Cadena f(Lleva texto  en '' y variables en {})
    return  f'El estudiante tiene una nota promedio de {promedio}, su mayor nota fue {maximo}, y su menor nota fue {minimo}' 
# para regresar un valor a la función
    '''pass'''
     # cuando no voy a definir nada por ahora y se borra cuando se completa la función


print(notas(3.5,4,4.6)) # con el print llamo la función y coloco los parámetros
print(notas(4,5,5))
print(notas(3,2,1))


