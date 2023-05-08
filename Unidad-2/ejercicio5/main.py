import os
from Menu import Menu
from Manejador import ManejadorPlan


if __name__ == '__main__':

    opcion = None
    menu = Menu()
    while opcion != 5:
        menu.mostrar()
        opcion = int(input('Tu ocpion: '))
        menu.menuOpciones(opcion)
    else:
            print('***Cerrando****')