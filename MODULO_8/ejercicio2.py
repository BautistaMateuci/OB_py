# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
from pickle import dump, load

class vehiculo():
    def __init__(self,marca):
        self.marca= marca
        
    def __str__(self):
        return 'el vehiculo es de la marca ' + self.marca 


a = vehiculo('corsa')
print(a)

archivo =open('MODULO_8/vehiculo_objeto', 'w+b')
dump(a, archivo)

archivo.seek(0)
nuevo_a = load(archivo)

print(nuevo_a)
archivo.close()