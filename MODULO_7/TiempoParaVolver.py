import time

hora = time.strftime("%H")
minutos = time.strftime('%M')


def go_to_home(hora):
    if int(hora) >= 19:
        print('Tu tiempo de trabajo a finalizado')
    else:
        print('Quedan {} horas y {} minutos para dejar de trabajar :('.format(18 - int(hora), 59 -(int(minutos))))

go_to_home(hora)