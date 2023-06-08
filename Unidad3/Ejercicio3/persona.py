class Persona:
    __nom: str
    __direc: str
    __dni: str
    __taller: object

    def __init__(self, nombre, direc, dni, taller) -> None:
        self.__nom = nombre
        self.__direc = direc
        self.__dni = dni
        self.__taller = taller

    def __str__(self) -> str:
        return f'Nombre: {self.getNombre()}, Direccion: {self.getDireccion()}, DNI: {self.getDni()}\n'

    def getNombre (self):
        return self.__nom

    def getDireccion (self):
        return self.__direc

    def getDni (self):
        return self.__dni

    def getTaller (self):
        return self.__taller