class ViajeroFrecuente():
    __numViajero=0
    __dni='dni'
    __nombre='nombre'
    __apellido='apellido'
    __millasAcum=1

    def __init__(self,numViajero=0,dni='',nombre='',apellido='',millasAcum=1):
        self.__numViajero=numViajero
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millasAcum=millasAcum

    def cantidadTotalMillas(self):
        print("Cantidad total de millas acumuladas es ->{ }",self.__millasAcum)

    def acumularMillas(self, millas):
        self.__millasAcum=int(self.__millasAcum)
        self.__millasAcum+=millas;
        print("Cantidad total de millas acumuladas es ->{ }", self.__millasAcum)

    def canjearMillas(self, millas):
        self.__millasAcum = int(self.__millasAcum)
        if millas<=self.__millasAcum:
            print("Millas Suficientes")
            self.__millasAcum=self.__millasAcum-millas
            print("Cantidad total de millas acumuladas es ->{ }", self.__millasAcum)
        else:
            print("La cantidad de millas es insuficiente")
            print("Cantidad total de millas acumuladas es ->{ }", self.__millasAcum)