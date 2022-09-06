# Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

# edad = int(input('Cual es tu edad? \n'))
def LEGAL_O_ILEGAL(edad):
    if edad >= 18:
        print('ya sos mayor :)')
    else:
        print('no sos mayor :(')

# Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
num = int(input('INTRODUCE EL NUMERO FINAL PARA SACAR IMPARES O PARES \n'))

for i in range(2, num):
    if i % 2 == 0:
        print(f'El numero {i} es par')
    else:
        print(f'el nuemro {i} es impar')


# Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.
num = 100
for i in range(0, num):
    print(num-i)



