class Inscripcion:
    __fecha: str
    __pago: bool
    __persona: object
    __taller: object

    def __init__(self, fecha, persona, taller, pago=False) -> None:
        self.__fecha = fecha
        self.__pago = pago
        self.__persona = persona
        self.__taller = taller

    def getFecha (self):
        return self.__fecha

    def getPago (self):
        return self.__pago

    def getPersona (self):
        return self.__persona

    def getTaller (self):
        return self.__taller

    def setPago (self):
        self.__pago = True
