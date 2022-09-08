# En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora: sumar, restar, multiplicar y dividir.
import operaciones as o


a = int(input('Que numero quieres poner \n'))
b = int(input('Que numero quieres poner \n'))
c = input('Quieres hacer suma, resta , multiplicacion o division \n')

def main():
    suma = o.suma
    resta = o.resta
    multiplicacion = o.multiplicacion 
    division = o.division
    
    if c == 'Suma' or c == 'suma':
        suma(a, b)
    elif c == 'Resta'  or c == 'resta':
        resta(a, b)
    elif c == 'Multiplicacion'  or c == 'multiplicacion':
        multiplicacion(a, b)
    elif c == 'Division'  or c == 'division':
        division(a, b)
    else:
        print('La opcion elegida no partenece a ninguna de operacion')
    


if __name__ == '__main__':
    main()