from Manejador import ManejadorPlan

class Menu:
    __instancia=None
    
    def __init__(self):
        self.__instancia = ManejadorPlan()
        self.__instancia.cargarObjetos()

    def mostrar(self):
        print('Menu de Opciones')
        print('1- Actualizar valor')
        print('2- Mostrar datos')
        print('3- Mostrar monto')
        print('4- Modificar cantidad cuotas')
        print('5- Salir')
        
    def opcion1(self):
        self.__instancia.modificar()

    def opcion2(self):
        self.__instancia.mostrarDatos()

    def ocpion3(self):
        self.__instancia.mostrarMonto()

    def ocpion4(self):
        self.__instancia.modificarCantidadCuotas()

    def menuOpciones(self,opcion):
        if opcion == 1:
            self.opcion1()
        elif opcion == 2:
            self.opcion2()
        elif opcion == 3:
            self.ocpion3()
        elif opcion == 4:
            self.ocpion4()