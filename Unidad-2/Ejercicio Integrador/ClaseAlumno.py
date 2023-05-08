class Alumno:
    __dni=''
    __apellido=''
    __nombre=''
    __carrera=''
    __anioCursa=0

    def __init__(self, dni='',apellido='', nombre='',carrera='',anioCursa=0):
        self.__dni=dni
        self.__apellido=apellido
        self.__nombre=nombre
        self.__carrera=carrera
        self.__anioCursa=anioCursa

    