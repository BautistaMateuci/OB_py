#En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.
archivo = open('MODULO_8/primer_archivo.txt', 'w')
archivo.write('Cree mi primer archivo en pithon!\n')
archivo.close

archivo = open('MODULO_8/primer_archivo.txt', 'r+')
archivo.readline()
archivo.write('Cree mi segunda linea en pithon!\n')

archivo.seek(0)
print(archivo.read())
archivo.close()
