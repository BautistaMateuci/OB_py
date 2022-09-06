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



        
class persona():
    
    def __init__(self):
        self.__Nombre =  'Juan'
        self.__Apellido = 'Gomez'
        self.__Edad = int(19)
        self.__Email = 'Juan.Gomez@gmail.com'
        self.__Telefono =  int(99999)
        self.__Casadx = False
        self.__Con_Hijxs = False
        self.__Lista_de_amigos = ['pedri', 'robert' , 'leo', 'gavi']
        self.__peliculas = {'pelicula1':'toy story', 
                    'pelicula2': 'cars', 
                    'pelicula3':'metegol'}
    
    def infopersona(self, hijx, casadx):
            self.__Casadx = casadx
            self.__Con_Hijxs =hijx
            
            if casadx == True:
                
                if hijx == True:
                    print(f'Hola me llamo {self.__Nombre} {self.__Apellido} y tengo {self.__Edad} anios\nmis amigos son {self.__Lista_de_amigos} amo estas peliculas {self.__peliculas.values()}, estoy casadx y tengo hijx\ny para contactarme te dejo mi telefono {self.__Telefono} y mi correo {self.__Email}')
                
                else:
                    print(f'Hola me llamo {self.__Nombre} {self.__Apellido} y tengo {self.__Edad} anios\nmis amigos son {self.__Lista_de_amigos} amo estas peliculas {self.__peliculas.values()}, estoy casadx y  no tengo hijx\ny para contactarme te dejo mi telefono {self.__Telefono} y mi correo {self.__Email}')
            
            elif casadx == False and hijx == True:
                print(f'Hola me llamo {self.__Nombre} {self.__Apellido} y tengo {self.__Edad} anios\nmis amigos son {self.__Lista_de_amigos} amo estas peliculas {self.__peliculas.values()}, no estoy casadx y tengo hijx\ny para contactarme te dejo mi telefono {self.__Telefono} y mi correo {self.__Email}')
            
            else:
                print(f'Hola me llamo {self.__Nombre} {self.__Apellido} y tengo {self.__Edad} anios\nmis amigos son {self.__Lista_de_amigos} amo estas peliculas {self.__peliculas.values()} no estoy casado ni tengo hijos\ny para contactarme te dejo mi telefono {self.__Telefono} y mi correo {self.__Email}')


x = persona()
print(x.infopersona(True, False))

print('===============================ACA PROBAMOS UN PROGRAMITA MAS UTIL===============================')

Peso = float(input('INTRODUCE TU PESO EN KG AQUI \n'))
Altura = float(input('INTRODUCE TU ALTURA EN METROS AQUI \n'))

def calculadorIMC(Peso, Altura):
    altm2 = Altura * Altura 
    return round(Peso / altm2 ,2)
print('tu imc es:', calculadorIMC(Peso,Altura))