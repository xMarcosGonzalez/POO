class PlanAhorro:
    __codP= 0
    __modelo= ""
    __version= ""
    __valorVehiculo= 0
    __cantCuotasP= 0
    __cantCuotasLicitar= 0

    def __init__(self, codP=0, modelo='', version='', valorVehiculo=0):
        self.__codP = codP
        self.__modelo = modelo
        self.__version = version
        self.__valorVehiculo = valorVehiculo

    def getcod(self):
        return self.__codP

    def muestra(self):
        return print('Codigo Plan: {} Modelo: {} Version: {}'.format(self.__codP,self.__modelo,self.__version))

    def setvalorVehiculo(self, valorNuevo):
        self.__valorVehiculo = valorNuevo
        print('Se cambio el valor')
    
    def getvalorVehiculo(self):
        return self.__valorVehiculo

    @classmethod
    def setcantCuotasP(cls, valor):
        cls.__cantCuotasP = valor

    @classmethod
    def setcantCuotasLicitar(cls, valor):
        cls.__cantCuotasLicitar = valor

    @classmethod
    def getcantCuotasP(cls):
        return cls.__cantCuotasP

    @classmethod
    def getcantCuotasLicitar(cls):
        return cls.__cantCuotasLicitar
        
    def __str__(self):
        return f'{self.__codP} {self.__modelo} {self.__version} {self.__valorVehiculo}'
    
    @classmethod
    def mostrar(cls):
        print('Cantidad cuotas: '+ (cls.getcantCuotasP()),end=' ')
        print('Cantidad cuotas a licitar: '+ (cls.getcantCuotasLicitar()))