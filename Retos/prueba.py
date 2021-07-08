
suma_notas = 0
cant_notas = 0
nota = 0

while nota >= 0:
    nota = float(input("Digite nota: "))
    if nota >= 0:
        suma_notas = suma_notas + nota
        cant_notas = cant_notas + 1
        print("La sumatoria de notas es: " + str(suma_notas) + ", para un total de " + 
            str(cant_notas) + " notas")

if cant_notas > 0:
    promedio = round(suma_notas / cant_notas, 1)
else:
    promedio = 0

print("El promedio de notas es: " + str(promedio))    
