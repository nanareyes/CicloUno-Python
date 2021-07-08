'''
El curso de Algoritmia y programación se califica con dos parciales (el primero tiene un peso de 30% y el segundo 35%),
una nota de laboratorios (25%) y una nota del trabajo final del curso (10%). Calcular la nota definitiva para un grupo 
de n estudiantes.

'''

# función para crear la definitiva 
def calcular_definitiva(p1, p2, lab, trab_final):
    definitiva = p1 * 0.30 + p2 * 0.25 + lab * 0.25 + trab_final * 0.1
    return (definitiva)


#Programa principal

numero_estudiantes = int(input("Ingrese el número de estudiantes: "))
i = 1
print('\n')

while (i <= numero_estudiantes):
    nombre = input("Digite el nombre del estudiante: ")
    parcial1 = float(input("Digite la nota del primer parcial: "))
    parcial2 = float(input("Digite la nota del segundo parcial: "))
    laboratorio = float(input("Digite la nota de Laboratorio: "))
    trabajo_final = float(input("Digite la nota del trabajo final:"))

    definitiva = calcular_definitiva(parcial1, parcial2, laboratorio, trabajo_final) # aquí llamo la función
    print(definitiva)
    
    print("La nota definitiva de ", nombre, "es:", definitiva) # aquí inserto el nombre (Variable) y llamo respuesta del while con definitiva 
    i +=1

print('\n')

