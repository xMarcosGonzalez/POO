import csv
from PlanAhorro import PlanAhorro

class ManejadorPlan:
    __listaobjetos=[]

    def __init__(self):
        self.__listaobjetos = []

    def cargarObjetos(self):
        archivo = open('planes.csv')
        reader = csv.reader(archivo, delimiter=';')
        for linea in reader:
            objeto = PlanAhorro(int(linea[0]),str(linea[1]),str(linea[2]),int(linea[3]))
            PlanAhorro.setcantCuotasP(int(linea[4]))
            PlanAhorro.setcantCuotasLicitar(int(linea[5]))
            self.__listaobjetos.append(objeto)

    def modificar(self):
        for obj in self.__listaobjetos:
            obj.muestra()
            valorNuevo= int(input('Ingrese el nuevo valor del vehiculo: '))
            obj.setvalorVehiculo(valorNuevo)

    def mostrarDatos(self):
        valor = int(input('Ingrese valor: '))
        for objetoo in self.__listaobjetos:
            valorcuota = (objetoo.getvalorVehiculo() / objetoo.getcantCuotasP())+objetoo.getvalorVehiculo()+0.10
            if valorcuota < valor:
                objetoo.muestra()
    
    def mostrarMonto(self):
        for ob in self.__listaobjetos:
            print('Plan %d' %ob.getcod())
            valorcuota= (ob.getvalorVehiculo() / ob.getcantCuotasP())+ob.getvalorVehiculo()+0.10
            monto=valorcuota*ob.getcantCuotasLicitar()
            print('Monto que debe haber pagado para licitar: ',monto)
    
    def modificarCantidadCuotas(self):
        cantidad = int(input('Ingrese la nueva cantidad de cuotas: '))
        PlanAhorro.setcantCuotasLicitar(cantidad)
        print('Se modifico')