from empleado import Empleado

class Contradado (Empleado):
    __fInicio: str
    __fFin: str
    __cantH: int # cantidad Horas Trabajadas
    __valorH: int # Valor Por Hora

    def __init__ (self, dni, nombre, direc, tel, fInicio, fFin, cantH, valorH):
        super().__init__ (dni, nombre, direc, tel)
        self.__fInicio = fInicio
        self.__fFin = fFin
        self.__cantH = cantH
        self.__valorH = valorH

    def getFechaInicio (self):
        return self.__fInicio

    def getFechaFin (self):
        return self.__fFin

    def getCantidadHoras (self):
        return self.__cantH

    def getValorHora (self):
        return self.__valorH

    def setCantidadHoras(self, c):
        self.__cantH += c