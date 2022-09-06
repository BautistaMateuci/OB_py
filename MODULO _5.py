#Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.

altura = 20
base = 100
def areatriangulo(altura, base):
    resultado = base * altura / 2
    print(resultado)

areatriangulo(altura,base)

#Escribe una función que pueda decirte si un número (número entero) es primo o no.

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

#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

year = int(1980)
def aniobisiesto(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('El year es bisiesto')
            else:
                print('El year no es bisiesto')
        else:
            print('El year es bisiesto.')
    else:
        print('El year no es bisiesto.')
    
        
aniobisiesto(year)


