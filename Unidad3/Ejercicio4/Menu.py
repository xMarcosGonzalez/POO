import os

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1: self.opc1,
                            2: self.opc2,
                            3: self.opc3,
                            4: self.opc4,
                            0: self.salir
                        }
        
    def opcion(self,op, mE):   ##manejador == manejador de la clase enviada desde el main
        func=self.__switcher.get(op, lambda: print("Opción no válida, intente de nuevo"))
        if op == 1 or op == 2 or op == 3 or op == 4:
            func( mE)
        else:
            func()

    def mostrarMenu(self):
        print("""
---------->Menu Principal<----------

-> 1: Registrar horas
-> 2: Total de tarea
-> 3: Ayuda Económica
-> 4: Calcular sueldos
-> 0: Salir del programa
""")

## OPCIONES

    def opc1 (self,  mE):
        os.system('cls')
        print ('---------->Registrar Horas<----------')
        dni = input ('Ingrese dni del empleado: ')
        mE.registrarHoras(dni)

    def opc2 (self,  mE):
        os.system('cls')
        print ('---------->Monto total de tarea<----------')
        tarea = input ('Ingrese tarea a buscar: ')
        total = mE.calcularMontoTarea(tarea)
        print (f'El monto total de la tarea sin terminar es: {total}')

    def opc3 (self,  mE):
        os.system('cls')
        print ('---------->Ayuda economica<----------')
        mE.ayudaEconomica()

    def opc4 (self, mE):
        os.system('cls')
        print ('---------->Sueldos de empleados<----------')
        mE.mostrarSueldos()

    def salir (self):
        print ('saliendo...')