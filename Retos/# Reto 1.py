# Reto 1
'''
La Academia Leonardo Davinci desea conocer el numero 
promedio de personas inscritas en el curso de Dibujo 
de Lunes a viernes
'''

def promedio_sumar(lunes, martes, miercoles, jueves, viernes):
    resultado = round((lunes + martes + miercoles + jueves + viernes)/5)
    return "El promedio de personas inscritas al curso de dibujo de lunes a viernes es: " + str(resultado)
'''
nro_inscritos_lunes = 50
nro_inscritos_martes = 80
nro_inscritos_miercoles = 100
nro_inscritos_jueves = 45
nro_inscritos_viernes = 30
'''
print('\n')
numero1 = float(input("Nro_inscritos_lunes : "))
numero2 = float(input("Nro_inscritos_martes : "))
numero3 = float(input("Nro_inscritos_miercoles : "))
numero4 = float(input("Nro_inscritos_jueves : "))
numero5 = float(input("Nro_inscritos_viernes : "))

promedio = promedio_sumar(numero1, numero2, numero3, numero4, numero5)
print('\n')
print (promedio)
print('\n')