import numpy as np
import csv
from datetime import datetime
from empleado import Empleado
from dePlanta import dePlanta
from externo import Externo
from contradado import Contradado

class Colecion:
    __cantidad = 0
    __dimension: int ## tamaño
    __incremento = 5

    def __init__(self, dimension, incremento = 5) -> None:
            self.__empleados = np.empty (dimension, dtype=Empleado)
            self.__cantidad = 0
            self.__dimension = dimension

    def addEmpleado (self, i):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__empleados.resize(self.__dimension, refcheck=False)
        self.__empleados[self.__cantidad] = i
        self.__cantidad += 1

    def cargas(self):
        self.cargaDePlanta()
        self.cargaContratados()
        self.cargaExternos()
        print ('Todos los empleados cargados con exito!')

    def cargaDePlanta (self):
        'Carga empleados de planta'
        path = './planta.csv'
        archivo = open (path, 'r')
        reader = csv.reader (archivo, delimiter=',')
        flag = True
        for fila in reader:
            if flag:flag = False
            else: 
                dni = fila [0]
                nom = fila [1]
                direc = fila [2]
                tel = fila [3]
                sueldo = int (fila [4])
                antig = int (fila [5])
                xEmpleado = dePlanta (dni, nom, direc, tel, sueldo, antig)
                self.addEmpleado(xEmpleado)

    def cargaContratados (self):
        'Carga empleados contratados'
        path = './contratados.csv'
        archivo = open (path, 'r')
        reader = csv.reader (archivo, delimiter=',')
        flag = True
        for fila in reader:
            if flag:flag = False
            else: 
                dni = fila [0]
                nom = fila [1]
                direc = fila [2]
                tel = fila [3]
                fechaInicio = fila [4]
                fechaFin = fila [5]
                cant = int (fila [6])
                valor = int (fila [7])
                xEmpleado = Contradado (dni, nom, direc, tel, fechaInicio, fechaFin, cant, valor)
                self.addEmpleado (xEmpleado)

    def cargaExternos (self):
        'Carga empleados externos'
        path = './externos.csv'
        archivo = open (path, 'r')
        reader = csv.reader (archivo, delimiter=',')
        flag = True
        for fila in reader:
            if flag:flag = False
            else: 
                dni = fila [0]
                nom = fila [1]
                direc = fila [2]
                tel = fila [3]
                tarea = fila [4]
                fechaInicio = [5]
                fechaFin = fila [6]
                montoV = int (fila [7])
                costo = int (fila [8])
                montoS = int (fila [9])
                xEmpleado = Externo (dni, nom, direc, tel, tarea, fechaInicio, fechaFin, montoV, costo, montoS)
                self.addEmpleado (xEmpleado)

    def buscarEmpleado (self, dni):
        valorRetorno=None
        bandera=False
        indice=0
        while (indice < len(self.__empleados) and not bandera):
            e = self.__empleados[indice]
            if (dni == e.getDni()):
                valorRetorno = self.__empleados[indice]
                bandera = True
            else:
                indice+=1
        return valorRetorno

    def registrarHoras( self, dni):
        e = self.buscarEmpleado (dni)
        if e != None:
            h = int (input ('Ingrese la cantidad de horas trabajadas en el día de la fecha: '))
            e.setCantidadHoras (h)
            print ('Se actualizó las horas trabajadas!')
            print (e.getCantidadHoras())
        else:
            print ('No se encontró el empleado')

    def calcularMontoTarea(self, tarea):
            total = 0
            fechaActual = datetime.now().date()
            fechaFormateada = fechaActual.strftime('%Y-%m-%d')
            print (fechaFormateada)
            for empleado in self.__empleados:
                if isinstance(empleado, Externo) and empleado.getTarea() == tarea and empleado.getFechaFin() != fechaFormateada:
                    total += empleado.getCostoObra()
            return total

    def sueldoPlanta (self, empleado): # Calculo sueldo empleado de planta
        basico = int (empleado.getSueldoBasico() / 100)
        return empleado.getSueldoBasico() + basico * empleado.getAntiguedad()

    def sueldoContratado (self, empleado): # Calculo sueldo empleado contratado
        return empleado.getCantidadHoras() * empleado.getValorHora()

    def sueldoExterno (self, empleado): # Calculo sueldo empleado externo
        return empleado.getCostoObra() - empleado.getMontoViatico() - empleado.getMontoSeguro()

    def ayudaEconomica (self):
        for empleado in self.__empleados:
            if isinstance (empleado, dePlanta):
                if self.sueldoPlanta(empleado) < 150000:
                    print (f'->{empleado.getNombre()}, {empleado.getDireccion()},{empleado.getDni()}')
            elif isinstance (empleado, Contradado):
                if self.sueldoContratado(empleado) < 150000:
                    print (f'->{empleado.getNombre()}, {empleado.getDireccion()},{empleado.getDni()}')
            else:
                if self.sueldoExterno(empleado) < 150000: 
                    print (f'->{empleado.getNombre()}, {empleado.getDireccion()},{empleado.getDni()}')

    def mostrarSueldos (self):
        for empleado in self.__empleados:
            if isinstance (empleado, dePlanta):
                print (f'->Nombre: {empleado.getNombre()}, telefono: {empleado.getTelefono()}, sueldo a cobrar: ${self.sueldoPlanta(empleado)}')
            elif isinstance (empleado, Contradado):
                print (f'->Nombre: {empleado.getNombre()}, telefono: {empleado.getTelefono()}, sueldo a cobrar: ${self.sueldoContratado(empleado)}')
            else: 
                print (f'->Nombre: {empleado.getNombre()}, telefono: {empleado.getTelefono()}, sueldo a cobrar: ${self.sueldoExterno(empleado)}')
