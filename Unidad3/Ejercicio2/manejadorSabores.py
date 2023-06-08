import csv
from sabor import Sabor

class manejadorSabores:
    __listaS: list

    def __init__(self) -> None:
        self.__listaS = []

    def __str__(self) -> str:
        s = ''
        for sabor in self.__listaS:
            s += str(sabor)
        return s

    def addSabor (self, s):
        self.__listaS.append(s)

    def carga (self):
        path = './Sabores.csv'
        file = open (path, 'r')
        reader = csv.reader (file, delimiter=';')
        flag = True
        for row in reader:
            if flag:
                flag = False
            else:
                idSabor = row[0]
                ing = row[1]
                nomSab = row[2]
                xSabor = Sabor (idSabor, ing, nomSab)
                self.addSabor(xSabor)
                print ('carga lista')
        file.close()

    def sumarContador (self, i):
        self.__listaS[i].sumarContador()

    def mostrarMejores(self):
        sabores_ordenados = sorted(self.__listaS, key=lambda sabor: sabor.getContador(), reverse=True)
        return sabores_ordenados[:5]

    def getSaborPorId (self, i):
        return self.__listaS[i]