import os

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1: self.opc1,
                            2: self.opc2,
                            3: self.opc3,
                            4: self.opc4,
                            5: self.opc5,
                            0: self.salir
                        }

    def opcion(self,op, mP, mT, mI):   ##manejador == manejador de la clase enviada desde el main
        func=self.__switcher.get(op, lambda: print("Opción no válida, intente de nuevo"))
        if op == 1 or op == 2 or op == 3 or op == 4 or op == 5:
            func(mP, mT, mI)
        else:
            func()

    def mostrarMenu(self):
        print("""
---------->Menu Principal<----------

-> 1: Inscribir una persona en un taller
-> 2: Consultar una inscripción
-> 3: Consultar inscriptos
-> 4: Registrar pago
-> 5: Guardar inscripciones
-> 0: Salir del programa
""")

## OPCIONES

    def opc1 (self, mP, mT, mI):
        os.system('cls')
        mT.darAlta(mP, mI)

    def opc2 (self, mP, mT, mI):
        os.system('cls')
        dni = input ('Ingrese dni del inscripto: ')
        mI.consultarInscripcion(dni)

    def opc3 (self, mP, mT, mI):
        os.system('cls')
        mT.mostrarTalleres()
        idT = int (input ('Ingrese el id del taller a consultar: '))
        mP.mostrarInscriptos(idT)

    def opc4 (self, mP, mT, mI):
        os.system('cls')
        dni = input ('Ingrese dni del inscripto: ')
        mI.registrarPago(dni)

    def opc5 (self, mP, mT, mI):
        os.system('cls')
        nombreArchivo = input ('ingrese nombre del archivo: ')
        nombreArchivo += '.csv'
        mP.generarArchivo(nombreArchivo)

    def salir (self):
        print ('saliendo...')