from empleado import Empleado

class dePlanta (Empleado):
    __sueldoBasico: int
    __antig: int

    def __init__ (self, dni, nom, direc, tel, sueldoB, antiguedad):
        super().__init__(dni, nom, direc, tel)
        self.__sueldoBasico = sueldoB
        self.__antig = antiguedad

    def getSueldoBasico(self):
        return self.__sueldoBasico

    def getAntiguedad (self):
        return self.__antig