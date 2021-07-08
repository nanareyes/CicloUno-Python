# 6. Crear un programa que reciba por teclado la edad de 10 personas e imprima por pantalla cuantos son mayores de edad y menores de edad hay en el grupo.


total_mayores = 0
total_menores = 0

for i in range(10):
    edad = int(input("Introduce la edad:"))
    if edad >= 18:
        total_mayores += 1
    else:
        total_menores += 1
print(
    "El total de las personas mayores es: ",
    total_mayores,
    "y el total de las personas menores es: ",
    total_menores,
)
