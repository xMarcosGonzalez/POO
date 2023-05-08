class Materias:
    __dni=''
    __nombreMateria=''
    __fecha=''
    __nota=0
    __aprobacion=''

    def __init__(self,dni='',nombreMateria='',fecha='',nota=0,aprobacion=''):
        self.__dni=dni
        self.__nombreMateria=nombreMateria
        self.__fecha=fecha
        self.__nota=nota
        self.__aprobacion=aprobacion
