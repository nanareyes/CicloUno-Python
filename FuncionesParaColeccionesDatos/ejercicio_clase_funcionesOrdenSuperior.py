"""
Una empresa recibe la información correspondiente a las ventas en pesos Colombianos de cada vendedro en el primer trimestre del año.
Se desea conocer el promedio de ventas en el trimestre por cada vendedor y el promedio en general de ventas en el trimestre.

Vendedores = ['Pedro López', 'Martha Jaramillo', 'Sandra Peña', 'Hugo Marín']
enero = [2000000, 1500000, 500000, 400000]
febrero = [1000000, 10000000, 800000, 200000]
marzo = [5000000, 600000, 3000000, 100000]

Imprimir por pantalla la información de la siguiente manera:
ventas_Enero = 0
ventas_Febrero = 0
ventas_Marzo = 0
promedio_de_ventas_trimestre = 0

============================================
Vendedor: Martha Jaramillo
Ventas Enero: $ 0000000
Ventas Febrero: $ 0000000
Ventas Marzo: $ 0000000
Promedio de ventas en el trimestre $ 0000000
============================================

"""

from statistics import mean


def promedio(a, b, c):
    return mean([a, b, c])


vendedores = ["Pedro López", "Martha Jaramillo", "Sandra Peña", "Hugo Marín"]
enero = [2000000, 1500000, 500000, 400000]
febrero = [1000000, 10000000, 800000, 200000]
marzo = [5000000, 600000, 3000000, 100000]


promedioventasTrimestre = list(map(promedio, enero, febrero, marzo))
promedio_final = mean(promedioventasTrimestre)
for x in range(0, len(vendedores)):
    print("Vendedor: {}".format(vendedores[x]))
    print("\n{} {}".format("Ventas Enero : $".ljust(14), enero[x]))
    print("{} {}".format("Ventas Febrero:$".ljust(14), febrero[x]))
    print("{} {}".format("Ventas Marzo : $".ljust(14), marzo[x]))
    print(
        "{} {}".format(
            "Promedio de Ventas en el Trimestre : $".ljust(14),
            round(promedioventasTrimestre[x], 2),
        )
    )

    print(format(" ".ljust(30, "=")))

print("\n" "Promedio de Ventas: {}".format(promedioventasTrimestre))
