import csv
import numpy as np
import os
from tallerCapacitacion import TallerCapacitacion as tc
from datetime import datetime

class ManejadorTalleres:
    __cantidad = 0
    __dimension = 0 ## tamaño
    __incremento = 5

    def __init__(self, dimension, incremento = 5) -> None:
            self.__taller = np.empty (dimension, dtype=tc)
            self.__cantidad = 0
            self.__dimension = dimension

    def addTaller (self, t):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__taller.resize(self.__dimension, refcheck=False)
        self.__taller[self.__cantidad] = t
        self.__cantidad += 1

    def carga (self):
        path = './Talleres.csv'
        file = open (path, 'r')
        flag = True
        reader = csv.reader (file, delimiter=';')
        for row in reader:
            if flag:
                flag = False
            else:
                idT = int(row [0])
                nom = row [1]
                vacante = int (row [2])
                monto = int (row [3])
                xtc = tc (idT, nom, vacante, monto)
                self.addTaller (xtc)
                print ('carga lista')
        file.close()

    def mostrarTalleres(self):
        for taller in self.getTalleres():
            print (str(taller))

    def darAlta (self, mP, mI):
        nom = input ('Ingrese nombre de la persona: ')
        direccion = input ('Ingrese direcion: ')
        dni = input ('Ingrese DNI de la persona: ')
        print ('Elija el taller a inscribir: ')
        self.mostrarTalleres()
        i = int (input ('Ingrese id del taller elegido: '))
        t = self.getTallerPorId(i-1)
        if t.getVacante() > 0:
            xPersona = mP.registrarPersona(nom, direccion, dni, t)
            inscripcion = mI.newInscripcion(xPersona, datetime.now().date(), t)
            t.addInscripcion(inscripcion)
            os.system('cls')
            print ('Persona inscripta con exito!')
            t.updateVacante()
        else: 
            os.system('cls')
            print ('Error, no hay vacantes para el taller. Vuelva a intentarlo')
            os.system('pause')
            os.system('cls')
            self.darAlta(mP, mI)

    def getTallerPorId (self, i):
        return self.__taller[i]

    def getTalleres(self):
        return self.__taller