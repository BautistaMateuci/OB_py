# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
# Color
# Ruedas
# Puertas
# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
# Velocidad
# Cilindrada
# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

class Vehiculo():
    
    def __init__(self, Color, Ruedas, Puertas):
        self.Color = Color
        self.Ruedas = Ruedas
        self.Puertas = Puertas

    def caracteristicas(self):
        print(f'Este Vehiculo es de color {self.Color}, tiene {self.Ruedas} ruedas y es un {self.Puertas} Puertas')
        
class Coche(Vehiculo):
    def __init__(self, Color, Ruedas, Puertas, Velocidad, Cilindrada):
        self.Color = Color
        self.Ruedas = Ruedas
        self.Puertas = Puertas
        self.Velocidad = Velocidad
        self.Cilindrada = Cilindrada
        
    def __str__(self):
        print(f'Este Vehiculo es de color {self.Color}, tiene {self.Ruedas} ruedas y es un {self.Puertas} Puertas, ademas va a una velocidad de {self.Velocidad} km/h gracias a sus {self.Cilindrada} cilindradas')

Juan = Coche('rojo', 4, 5, 300, 150)
print(Juan.__str__())


# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
class Alumno():
    
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        
    def aprobo_o_desaprobo(self):
        if self.nota >= 5 :
            print(f'el alumno {self.nombre} aprobo la materia con nota {self.nota} felicidades !')
        else:
            print(f'el alumno {self.nombre} desaprobo la materia con nota {self.nota} a estudiar mas !')


x = Alumno('agustin',6)
x.aprobo_o_desaprobo()