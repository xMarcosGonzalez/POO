import os
from Menu import Menu
from coleccion import Colecion

if __name__ == '__main__':
    tamaño = int (input ('Ingrese cantidad de empleados: '))
    mE = Colecion (tamaño)
    mE.cargas()
    bandera = False
    os.system ('pause')
    os.system('cls')
    menu = Menu()
    while not bandera:
        menu.mostrarMenu()
        opcion = int (input("Su opcion: "))
        menu.opcion(opcion, mE)
        if opcion == 0:
            bandera = True
        os.system('pause')
        os.system('cls')
    os.system('exit')