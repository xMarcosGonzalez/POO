import os
from manejadorPersona import manejadorPersona
from manejadorTalleres import ManejadorTalleres
from manejadorInscripcion import manejadorInscripcion
from Menu import Menu

if __name__ == '__main__':
    mP = manejadorPersona()
    mT = ManejadorTalleres(3)
    mI = manejadorInscripcion(3)
    mT.carga()
    bandera = False
    os.system('cls')
    menu = Menu()
    while not bandera:
        menu.mostrarMenu()
        opcion = int (input("Su opcion: "))
        menu.opcion(opcion, mP, mT, mI)
        if opcion == 0:
            bandera = True
        os.system('pause')
        os.system('cls')
    os.system('exit')
