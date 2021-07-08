# Ejercicio 1
for i in range(0, 6):
    print("Numero ", i)

# Ejercicio 2
for i in range(0, 10, 2):
    print("Estamos en la iteración " + str(i))

# Ejercicio 3
for i in range(18, 10, -2):
    print("Numero " + str(i))

# Ejercicio 4
for i in range(0, 20):
    if i % 2 == 0:
        print("El valor de i es ", i)

# Ejercicio 5
for k in range(0, 5, 2):
    a += 1  # contador
    print("El valor de k es: ", k)

print("---------------------")
print("El valor de a es: " + str(a))

# Ejercicio 6
total = 0
for i in range(5):
    nuevoNumero = int(input("Introduce un número: "))
    total += nuevoNumero
print("El total es: ", total)

# Ejercicio 7
secuencia = ["uno", "dos", "tres"]
for elemento in secuencia:
    print(elemento)


# Ejercicio 8
total = 0
for i in range(5):
    nuevoNumero = int(input("Introduce un número: "))
    if nuevoNumero == 0:
        total += 1
print("Has introducido ", total, " ceros")
