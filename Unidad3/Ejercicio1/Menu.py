from ManejadorFacultades import ManejadorFacultad


class Menu:
    __insntacia: ManejadorFacultad

    def __init__(self):
        self.__instancia = ManejadorFacultad()
    
    def mostrar(self):
        print('Menu de Opciones')
        print('1- Cargar Estructuras')
        print('2- Mostrar Nombre Facultad y duracion de sus carreras')
        print('3- Mostrar Codigo de Facultad-Carrera, Nombre y Localidad')
        print('0- Salir')

    def opcion1(self):
        print('\n')
        self.__instancia.cargarFacultades()
        print('Estructuras Cargadas')

    def opcion2(self):
        print('\n')
        codigo = int(input('Ingrese un codigo de Facultad: '))
        self.__instancia.buscarFacultad(codigo)

    def opcion3(self):
        print('\n')
        carrera = input('Ingrese el nombre de Carrera: ')
        self.__instancia.buscarCarrera(carrera)

    def menuopciones(self,opcion):
        if opcion == 1:
            self.opcion1()
        elif opcion == 2:
            self.opcion2()
        elif opcion == 3:
            self.opcion3()
        elif opcion != 1 or opcion != 2 or opcion != 3:
            print('Opcion no Valida')

    