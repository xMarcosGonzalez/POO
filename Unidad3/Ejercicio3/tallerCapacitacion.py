class TallerCapacitacion:
    __idTaller: int
    __nom: str
    __vacante: int
    __montoInscripcion: int
    __inscripcion: object

    def __init__(self, idTaller, nom, vacante, monto, inscripcion=None) -> None:
        self.__idTaller = idTaller
        self.__nom = nom
        self.__vacante = vacante
        self.__montoInscripcion = monto
        if inscripcion != None:
            self.addInscripcion(inscripcion)

    def __str__(self) -> str:
        return f'idTaller: {self.getIdTaller()}, Nombre del Taller: {self.getNombreTaller()}, Vacante: {self.getVacante()}, Monto de Inscripcion: {self.getMonto()}'

    def addInscripcion (self, inscripcion):
        self.__inscripcion = inscripcion

    def updateVacante(self):
        self.__vacante -= 1

    def getIdTaller (self):
        return self.__idTaller

    def getNombreTaller (self):
        return self.__nom

    def getVacante (self):
        return self.__vacante

    def getInscripcion (self):
        return self.__inscripcion

    def getMonto (self):
        return self.__montoInscripcion