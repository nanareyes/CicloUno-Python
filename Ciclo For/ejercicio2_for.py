# 2. Leer 5 personas y pedir salario. Imprimir sumatoria de salario.

suma_salario = 0

for i in range(5):
    salario = int(input("Ingrese el salario: "))
    suma_salario = suma_salario + salario
print("La suma de los salarios es: ", suma_salario)
