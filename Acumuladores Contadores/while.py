'''
Mientras que (While)

El Ciclo Mientras que es conocido en los lenguajes de programación como 
ciclo While, una de sus características es que verifica si la condición 
se cumple antes de ingresar al bloque de código que se va a repetir, el 
límite de ejecuciones estará dado por la condición, se ejecutará mientras 
la condición devuelva un valor lógico verdadero.

mientras  {condición}     
            acción    1  
            acción    2    
            acción    3    
             .....    
            acción  n       
ﬁn  mientras    
instrucción  X    
'''

x = 5
while x > 0:
    x -= 1 # x == x - algo Ej: x == a -1
    print(x)


