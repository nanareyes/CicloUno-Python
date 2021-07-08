from statistics import mean


vendedores = ["Mario Correa", "Martha Ramírez", "Sandra Peña", "Hugo López"]
ventasEnero = [900000000, 600000000, 400000000, 180000000]
ventasFebrero = [100000000, 450000000, 100000000, 200000000]
ventasMarzo = [460000000, 120000000, 500000000, 700000000]


def imprimir_resultados() -> str:
    for x in range(0, len(vendedores)):
        print("Vendedor: {}".format(vendedores[x]))
        print(
            "\n{} {}".format("Ventas Enero :".ljust(14), "{:,}".format(ventasEnero[x]))
        )
        print(
            "{} {}".format(
                "Ventas Febrero :".ljust(14), "{:,}".format(ventasFebrero[x])
            )
        )
        print("{} {}".format("Ventas Marzo :".ljust(14), "{:,}".format(ventasMarzo[x])))
        ventas = [ventasEnero[x], ventasFebrero[x], ventasMarzo[x]]
        promedioventasTrimestre = round(mean(ventas))
        print(
            "{} {}".format(
                "Promedio Ventas Trimestre :".ljust(14),
                "{:,}".format(
                    promedioventasTrimestre,
                ),
            )
        )
        print(
            "Meta: {}".format(
                "Se alcanzó la meta del promedio de ventas en el Trimestre"
                if promedioventasTrimestre > 500000000
                else "No se alcanzó la meta del promedio de ventas en el Trimestre"
            )
        )
        print("\n{}".format("".ljust(54, "=")))


imprimir_resultados()
