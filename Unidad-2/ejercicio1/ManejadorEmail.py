
import csv
from ClaseEmail import Email

class ListaManejador:
    __lista = []

    def __init__(self):
        self.__lista = []
    def leerArchivo(self):
        archivo = open('listaemail.csv')
        reader = csv.reader(archivo, delimiter=',')

        cvarias = Email()

        for linea in reader:
            print("cuenta-> \n",linea[0])
            cvarias.CrearCuenta(linea[0])
            correo=linea[0]
            correo = correo.split('@')
            correo=correo[1].split('.')
            self.__lista.append(correo[0])


    def buscarDominio(self, dom,):
        c = 0
        for i in self.__lista:
            if i == dom:
                c = c + 1

        print("La cantidad de cuentas cn el mismo dominio es de:", c)