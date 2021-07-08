'''
La empresa “La TVE” ha decidido implementar un nuevo sistema de salarios para mejorar su clima organizacional. Las nuevas normas de incremento son:
•	Si es obrero, se incrementa un 10 por ciento. 
•	 Si es ingeniero y gana menos de 1’000.000, aumento del 8%.
•	 Si es ingeniero y gana entre de 1’000.001 y 2’000.000, incrementa el 6%.
•	 Si es ingeniero y gana entre de 2’000.001 y 3’000.000, el salario sube un 5%. 
•	 Si es ingeniero y gana entre de 3’000.001 y 4’000.000, hay un aumento del 3%. 
•	 Si es ingeniero y gana entre de 3’000.001 y 4’000.000 y se llama Ruperto Mena, se incrementa en 4%.
•	 Si es ingeniero y gana más de 4’000.000, un alza de 8 porciento.
•	 Si es publicista y gana más de 1’500.000, incrementa en $150.000. 
•	 Si es gerente se sube el salario un 2 %. 

Por lo anterior, debe desarrollarse un algoritmo que implemente estas modificaciones al sistema de salarios y nos muestre en pantalla el nombre, cargo, 
salario inicial, incremento y salario final del empleado.

'''
'''
ALGORITMO

Entradas: 
    cargo
    salario
    incrementos

Proceso: salario * incremento

Salida: 
nombre
cargo
salario inicial
incremento
salario final
'''

def incremento_salario(c,s,n):
    if c == "obrero":
        return s * 0.1
    elif c == "ingeniero":
        if n == "Ruperto Mena":
            return s * 0.04
        else:
            if s < 1000000:
                return s * 0.08
            elif s >= 1000001 and s<= 2000000:
                return s * 0.06
            elif s >= 2000001 and s<= 3000000:
                return s * 0.05
            elif s >= 3000001 and s<= 4000000:
                return s * 0.03
    elif c == "publicista":
        if s >= 1500000:
            return (150000)
    elif c == "gerente":
        return s * 0.02

    return s * 0

print('\n')
nombre = input("Digite el Nombre: ")
cargo = input("Digite el cargo: ")
salario = int(input("Digite el salario: "))
resultado = incremento_salario(cargo, salario,nombre)
print('\n')

print("Nombre: ", nombre)
print ("Cargo: ",cargo)
print ("El salario inicial fue: ", salario)
print("El incremento del salario es:", round(resultado))
print("el valor del salario final es: ", round(salario + resultado))
print('\n')

'''
Ruperto Mena
ingeniero
4000000
'''