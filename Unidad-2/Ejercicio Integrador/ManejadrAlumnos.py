import numpy
import csv
from ClaseAlumno import Alumno
class ManejadorAlumnos:
    __lista=[]

    def __init__(self):
        self.__lista=[]

    def cargarAlumnos(self):
        archivo = open('alumnos.csv')
        reader = csv.reader(archivo, delimiter=',')

        for linea in reader:
            objeto = Alumno(int(linea[0]),int(linea[1]),bool(linea[2]),linea[3],linea[4])
            lista.append(objeto)
        self.__listaobjetos = numpy.array(lista,dtype=Alumno)

    def buscarMostrar(self, nombre):
        i= 0
        valor= 0
        while i < len(self.__listaobjetos) and nombre != self.__listaobjetos[i].getnya():
            i += 1
        else:
            if i < len(self.__listaobjetos):
                fechaA = input('Ingrese: ')
                valor = self.__listaobjetos[i].get()
                self.__listaobjetos[i].set()
                self.__listaobjetos[i].mostrar()
            else:
                print('')
        return valor

    def listar(self, s):
        for objeto in self.__listaobjetos:
            if objeto.get():
                if s == objeto.ge():
                    objeto.mostra()


