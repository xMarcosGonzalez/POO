from __future__ import annotations


class Conjunto:
    __lista=[]

    def __init__(self, num=0):
        self.__lista = num
    
    def __repr__(self):
        lista =self.__lista[1:-1]
        return "Conjunto {"+(lista)+"}"
    
    def __add__(self,Conjunto):
        self.__lista.sort()
        listaResultante = self.__lista
        otro.__lista.sort()
        for objetoI in otro.__lista:
            if objetoI not in listaResultante:
                listaResultante.append(objetoI)
        return Conjunto(listaResultante)

    def __sub__(self, otro:Conjunto):
        self.__lista.sort()
        otro.__lista.sort()
        listaResultante= []
        for objeto in self.__lista:
            if objeto not in otro.__lista:
                listaResultante.append(objeto)
        return Conjunto(listaResultante)
    
    def __eq__(self,Conjunto):
        valor = None
        if len(self.__lista) == len(otro.__lista):
            for objetoI in self.__lista:
                for objetoJ in otro.__lista:
                    if(objetoI==objetoJ):
                        valor =True
                    else:
                        valor = False
        return valor



