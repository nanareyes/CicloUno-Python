# contador de un número en particular

total = 0

for i in range(5):
    nuevonumero = int(input("Introduce un número:"))
    if nuevonumero == 0:
        total += 1
print("Has introducido: ", total, "ceros")
