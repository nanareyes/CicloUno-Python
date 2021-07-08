# Programación funcional
# Minimizar el número de asignaciones
# Funciones de primera clase (variables), funciones de orden superior (reciben o retornan funciones)


def operacion(signo):
    if signo == "+":

        def suma(a=0, b=0):
            return a + b

        return suma

    elif signo == "-":

        def resta(a=0, b=0):
            return a - b

        return resta

    else:

        def funcion(a, b):
            return (a, b)

        return funcion


def calculadora(signo, a, b):
    # Dependiendo del signo que reciba, solicita la construcción de una función
    funcionGenerada = operacion(signo)
    return funcionGenerada(a, b)


print("Calculadora Funcional")
print(calculadora(input("Signo ->"), int(input("a->")), int(input("b->"))))
print(calculadora(input("Signo ->"), int(input("a->")), int(input("b->"))))
print(calculadora(input("Signo ->"), int(input("a->")), int(input("b->"))))
