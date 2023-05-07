import csv
from ClaseViajero import ViajeroFrecuente

class Manejador:
    __lista = []

    def __init__(self):
        self.__lista = []

    def leerArchivo(self):
        archivo = open('viajeros.csv')
        reader = csv.reader(archivo, delimiter=',')

        for linea in reader:
            unViajero = ViajeroFrecuente(linea[0], linea[1], linea[2], linea[3], linea[4])
            self.__lista.append(unViajero)

    def cantViajeros(self):
        return len(self.__lista)
    def menu(self, numV):
        """menu"""
        print("<<<MENU DE OPCIONES>>> \n"
              "(1). CONSULTAR CANTIDAD DE MILLAS\n"
              "(2). ACUMULAR MILLAS\n"
              "(3). CANJAER MILLAS\n"
              "(0). SALIR")

        opcion = int(input("Seleccione la opcion ->"))

        if opcion == 1:
            self.__lista[numV - 1].cantidadTotalMillas()
        elif opcion == 2:
            millasA = int(input("Ingrese cantidad de millas a acumular -> "))
            self.__lista[numV - 1].acumularMillas(millasA)
        elif opcion == 3:
            millasC = int(input("Ingrese cantidad de millas a canjear -> "))
            self.__lista[numV - 1].canjearMillas(millasC)
        elif opcion == 0:
            print("Cerrando....")