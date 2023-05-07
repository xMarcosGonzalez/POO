
import csv
from ManejadorViajeros import Manejador
if __name__ == '__main__':

    lista=Manejador()
    lista.leerArchivo()

    numV=int(input("Ingresa un número de viajero frecuente -> "))
    cant=int(lista.cantViajeros())
    if numV<=cant:
        lista.menu(numV)
    else: print("El Viajero no existe")









