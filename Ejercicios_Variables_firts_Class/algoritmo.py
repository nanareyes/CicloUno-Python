'''
Se desea calcular la distancia recorrida (m) por un movil que tiene
una velocidad constante (m/s) durante un tiempo t(seg)
considerar que es un movimiento rectilineo uniforme 
'''

'''
ENTRADAS
velocidad (m/s) =  v
Tiempo (seg) = t

PROCESOS
d = v * t

SALIDAS
Diferencia recorrida  = d
'''

#Algoritmo
'''
INICIO
    leerv
    leert
    d = v * t
    Escribir D
FIN
'''

def multiplicar(v,t):
    d = v * t
    return d

'''
v =int(input("Digite la velocidad (m/s) : "))
t =int(input("Digite el tiempo (seg): "))
d = multiplicar(v,t)
print("La distancia recorrida es : ",d)
'''
v =int(input("Digite la velocidad (m/s) : "))
t =int(input("Digite el tiempo (seg): "))
print("La distancia recorrida es : ",multiplicar(v,t))



