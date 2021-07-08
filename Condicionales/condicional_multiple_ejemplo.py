'''
Calcular la utilidad que un trabajador recibe en el
reparto anual de utilidades si este se le asigna como
un porcentaje de su salario mensual que depende de su
antigüedad en la empresa de acuerdo con la siguiente


Tiempo
menosde 1 año                   5% del salario
1 año o más y menos de 2 años   7% del salario
2 años y menos de 5 años        10% del salario
5 años y menos de 10 años       15% del salario
10 años o mas                   20% del salario


ALGORITMO

Inicio
 sm,antig: Entero
 LEER sm, antig
 Si antig < 1  entonces
             util = sm * 0.05
     Si No
           Si (antg >= 1)  and (antig < 2) entonces
                         util = sm * 0.07
                    Si no
                           Si (antig >= 2)  and (antig < 5) entonces
                                       util = sm * 0.10
                                 Si no
                                   Si (antig >= 5)  and (antig < 10) entonces
                                                         util = sm * 0.15
                                                Si no
                                                         util = sm * 0.20
                                     Fin Si
                           Fin Si
               Fin Si
     Fin Si
     imprimir “La utilidad es: ”,util
Fin

'''

salario = int(input("Digite el salario mensual: "))
antiguedad = int(input("Digite años de antiguedad en la empresa: "))

if antiguedad <= 1:
    utilidad = round(salario * 0.05)
else:
    if (antiguedad >= 1) and (antiguedad < 2):
        utilidad = round(salario * 0.07)
    else:
        if (antiguedad >= 2) and (antiguedad < 5):
            utilidad = round(salario * 0.10)
        else:
            if(antiguedad >=5) and (antiguedad < 10):
                utilidad = round(salario * 0.15)
            else:
                utilidad = round(salario * 0.20)

print("La utilidad es: ", utilidad)