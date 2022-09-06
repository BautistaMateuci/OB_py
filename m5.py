# Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.

altura = 20
base = 100
def areatriangulo(altura, base):
    resultado = base * altura / 2
    print(resultado)

areatriangulo(altura,base)

# Escribe una función que pueda decirte si un número (número entero) es primo o no.

numerito = int(input('Introduce el numero para ver si es primo o no :) \n'))
def primo(numerito):
    if type(numerito) == float:
        print("No es un numero entero")
        return False

    for i in range(2, numerito):
        if numerito % i == 0:
            print(numerito, "No es primo", i, "es divisor")
            return False
    print(numerito, "Es primo")
    return True

primo(numerito)

# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

año = int(1980)
def aniobisiesto(año):
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                print('El año es bisiesto')
            else:
                print('El año no es bisiesto')
        else:
            print('El año es bisiesto.')
    else:
        print('El año no es bisiesto.')
    
        
aniobisiesto(año)

