import _thread
import time
import logging
from functools import reduce
# Crea un script que le pida al usuario una lista de países (separados por comas).
# Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). 
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

a = input('introduce paises separados por una coma: \n')

paises = [pais for pais in a.split(',')]

print(",".join(sorted(set(paises))))

# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter
# y realizará una suma de todos estos elementos obtenidos mediante reduce.


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def suma(a, b):
    return a + b

def mifuncion(x):
    if x % 2 == 0:
        return False
    
    return True

resultado =(filter(mifuncion, numeros))
print(reduce(suma, resultado))


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# def horaActual(nombre_thread, tiempo_de_espera):
#     count = 0
    
#     while count < 5:
#         time.sleep(tiempo_de_espera)
#         count += 1
#         print(f' hilo: {nombre_thread} - {time.ctime(time.time())}')


# _thread.start_new_thread(horaActual, ('uno', 1))
# _thread.start_new_thread(horaActual, ('dos', 5))

# print('dispare todos los hilos')
# while True:
#     pass


# logging.basicConfig(level=logging.INFO)
# logging.debug('soy el mas easy')
# logging.info('arrancamos?')
# logging.warning('mepa q no')
# logging.error('meparece que no')
# logging.critical('NO VAMOS A NINGUN LADOOOO!')



# def mifuncion(x):
#     if x % 2 == 0:
#         return True
    
#     return False

# resultado = filter(mifuncion, numeros)
# print(list(resultado))


# def cuadrado(x):
#     return x * x

# resultado = map(cuadrado, numeros)
# print(list(resultado))


# def suma(a, b):
#     return a + b

# res = reduce(suma, numeros)
# print(res)

# cursos = ['java', 'python', 'git']
# asistentes = [1, 40 , 1]

# demo = zip(cursos, asistentes)
# print(list(demo))

# listA = [1 == 2, 2 == 2, 3 == 4]

# res = any(listA)
# print(res)


# a = 5.5
# b = 6.8
# c = 6.4

# print(round(b))
# print(round(a))
# print(round(c))


# print(min(2, 4, 5, 6))
# print(pow(2, 4))

# from getpass import getpass

# user = input('nombre')
# passwd = getpass('pass')
# print(user, passwd)

# secreto = 50
# valor = 0



# while valor != secreto:
#     valor = int(input('introduce un numero :\n'))
    
#     if valor > secreto:
#         print('muy alto')
#         continue

#     if valor< secreto:
#         print('muy bajo')
#         continue
# print('acertaste !')            