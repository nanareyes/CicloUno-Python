salario = int(input("Digite el salario mensual: "))
antiguedad = int(input("Digite años de antiguedad en la empresa: "))

if antiguedad <= 1:
    utilidad = (salario * 0.05)
else:
    if (antiguedad >= 1) and (antiguedad < 2):
        utilidad = (salario * 0.1)
    else:
        if (antiguedad >= 2) and (antiguedad < 5):
            utilidad = (salario * 0.15)
        else:
            if(antiguedad >=5) and (antiguedad < 10):
                utilidad = (salario * 0.2)
print("La utilidad es: ", round(utilidad))
