'''
#Para explicar Try y Except utilizaremos de ejemplo una función que convierte la temperatura en grados Fahrenheit a una temperatura en grados Celsius: 

temperatura_fahr = input('Ingrese la temperatura en grados Fahrenheit: ')
fahr = float(temperatura_fahr)
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)

'''


temperatura_fahr = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(temperatura_fahr)
    cel =  5.0 / (9.0 * (fahr - 32.0))
    print(cel)
except:
    print('Please enter a number')
  