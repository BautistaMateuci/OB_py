# Para este ejercicio tenéis que crear en la consola de python variables que representen los siguientes datos de un contacto:
# Nombre
# Apellidos
# Edad
# Email
# Teléfono
# Casado (verdadero o falso)
# Con Hijos (verdadero o falso)
# Lista de amigos
# Películas vistas (diccionario con clave y valor. El valor será el título de la película)
# Una vez hayas creado todas las variables, muéstralas por consola haciendo uso de la función print().

Nombre =  'Juan'
Apellido = 'Gomez'
Edad = int(19)
Email = 'Juan.Gomez@gmail.com'
Telefono =  int(99999)
Casadx = False
Con_Hijxs = False
Lista_de_amigos = ['pedri', 'robert' , 'leo', 'gavi']
peliculas = {'pelicula1':'toy story', 'pelicula2': 'cars', 'pelicula3':'metegol'}
print(Nombre)
print(Apellido)
print(Edad)
print(Email)
print(Telefono)
print(Casadx)
print(Con_Hijxs)
print(Lista_de_amigos)
print(peliculas.values())
print('===============================ACA PROBAMOS UN PROGRAMITA MAS UTIL===============================')

Peso = float(input('INTRODUCE TU PESO EN KG AQUI \n'))
Altura = float(input('INTRODUCE TU ALTURA EN METROS AQUI \n'))

def calculadorIMC(Peso, Altura):
    altm2 = Altura * Altura 
    return round(Peso / altm2 ,2)
print('tu imc es:', calculadorIMC(Peso,Altura))