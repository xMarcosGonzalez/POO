import csv
from persona import Persona

class manejadorPersona:
    __listaP: list

    def __init__(self) -> None:
        self.__listaP = []

    def addPersona(self, p):
        self.__listaP.append (p)

    def registrarPersona(self, nom, direc, dni, t):
        xPersona = Persona (nom, direc, dni, t)
        self.addPersona (xPersona)
        return xPersona

    def mostrarInscriptos (self, idT):
        for persona in self.__listaP:
            t = persona.getTaller()
            if t.getIdTaller() == idT:
                print (str (persona))

    def generarArchivo (self, nombre_archivo):
        encabezados = ['DNI', 'idTaller', 'fechaInscripcion', 'pago']
        with open(nombre_archivo, 'w', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv, delimiter=';')
            writer.writerow(encabezados)
            for persona in self.__listaP:
                dato = [persona.getDni(), persona.getTaller().getIdTaller(), persona.getTaller().getInscripcion().getFecha(), persona.getTaller().getInscripcion().getPago()]
                writer.writerow(dato)
        print(f"Se ha generado el archivo CSV '{nombre_archivo}' con éxito.")



'''
git remote add origin https://github.com/Tima-Zotelo/u3POO-Actividad3.git
git branch -M main
git push -u origin main
'''
