class Empleado:
    __dni: str
    __nombre: str
    __direc: str
    __tel: int

    def __init__(self, dni, nombre, direc, tel) -> None:
        self.__dni = dni
        self.__nombre = nombre
        self.__direc = direc
        self.__tel = tel

    def getDni(self):
        return self.__dni

    def getNombre (self):
        return self.__nombre

    def getDireccion (self):
        return self.__direc

    def getTelefono (self):
        return self.__tel