from empleado import Empleado

class Externo (Empleado):
    __tarea: str
    __fInicio: str
    __fFin: str
    __montoViatico: int
    __costoObra: int
    __montoSeguro: int

    def __init__ (self, dni, nombre, direc, tel, tarea, fInicio, fFin, montoV, costo, montoS):
        super().__init__(dni, nombre, direc, tel)
        self.__tarea = tarea
        self.__fInicio = fInicio
        self.__fFin = fFin
        self.__montoViatico = montoV
        self.__costoObra = costo
        self.__montoSeguro = montoS

    def getTarea (self):
        return self.__tarea

    def getFechaInicio (self):
        return self.__fInicio

    def getFechaFin (self):
        return self.__fFin

    def getMontoViatico (self):
        return self.__montoViatico

    def getCostoObra (self):
        return self.__costoObra

    def getMontoSeguro (self):
        return self.__montoSeguro