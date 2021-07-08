experiencia = -1
salario = 2000000

# si tiene más de dos de exp el bono es de 100000
# Si tiene cuatro años o más de exp el bono es de 200000
# Si tiene seis años o más de exp el bono es de 300000

if experiencia > 2 and experiencia < 4:
    salario = salario + 100000
elif experiencia >= 4 and experiencia < 6:
    salario = salario + 200000
elif experiencia >= 6:
    salario = salario + 300000
else:
    print("Aún no cumples con la experiencia necesaria")  # salario = salario + 300000

print(salario)
