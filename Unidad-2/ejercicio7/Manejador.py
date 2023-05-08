import csv
from ViajeroFrecuente import ViajeroFrecuente

class ManejadorViajero:
    __listaobjetos=[]
    def __init__(self):
        self.__listaobjetos = []

    def cargarViajero(self):
        archivo = open('viajeros.csv')
        reader = csv.reader(archivo, delimiter=',')
        cont = 0
        for lineaA in reader:
            objeto = ViajeroFrecuente(int(lineaA[0]), (lineaA[1]), (lineaA[2]), lineaA[3], int(lineaA[4]))
            self.__listaobjetos.append(objeto)
            cont += 1

    def buscar(self):
        j=0
        numero = int(input('Ingrese el numero de viajero frecuente: '))
        
        while j < len(self.__listaobjetos) and numero != self.__listaobjetos[j].getnumero():
            j+=1
        if j < len(self.__listaobjetos):
            posicion = j
            print(f'Encontrado: posicion: {posicion+1}')
        else:
            print('No coinciden')

    def consultarMillas(self):
        cant1 = self.__listaobjetos[posicion].cantidadTotalMillas()
        print('La cantidad total de millas acumuladas es {}\n'.format(cant1))

    def acumular(self):
        cant2 = int(input('Ingrese la cantidad de millas recorridas: '))
        valor1 = self.__listaobjetos[posicion].acumularMillas(cant2)
        print('Valor actualizado de las millas: {}\n'.format(valor1))
    
    def canjear(self):
        cant3 = int(input('Ingrese la cantidad de millas a canjear: '))
        valor2 = self.__listaobjetos[posicion].canjerarMillas(cant3)
        print('Valor de cantidad de millas acumuladas: {}\n'.format(valor2))

    def maximo(self):
        i = 0
        maximo = self.__listaobjetos[0]
        for objeto in self.__listaobjetos:
            if objeto[i] > maximo:
                maximo = objeto[i]
            i+=1
        i = 0
        for objeto in self.__listaobjetos:
            if maximo == objeto[i].cantidadTotalMillas():
                print(objeto[i].muestra)
    
    def acumularSobrecargar(self):
        for objeto in self.__listaobjetos:
            cant2 = int(input('Ingrese la cantidad de millas recorridas: '))
            objeto.__millas_Acum = objeto.__millas_acum + cant2

    def maximo(self):
        maximo = self.__listaobjetos[0]
        for objeto in self.__listaobjetos:
            if objeto > maximo:
                maximo = objeto
        for objeto in self.__listaobjetos:
            if maximo.cantidadTotalMillas() == objeto.cantidadTotalMillas():
                print(objeto.muestra())
    
    def acumularSobrecargar(self):
        i=0
        for objeto in self.__listaobjetos:
            i+=1
            print('\nViajero (%d)' %i)
            cant2 = int(input('Ingrese la cantidad de millas recorridas: ')) 
            objeto = objeto + cant2
            print(objeto.muestra())

    
    def canjearSobrecarga(self):
        i=0
        for objeto in self.__listaobjetos:
            i+=1
            print('\nViajero ()',i)
            cant2 = int(input('Ingrese la cantidad de millas a canjear: ')) 
            objeto = objeto - cant2  
            print(objeto.muestra())
    

    #Ejercicio 7
    def compararSobrecargar(self):
        print('\n')
        print('Comparar')
        valor = int(input('Ingrese el valor a comparar: '))
        for objeto in self.__listaobjetos:
            if objeto == valor:
                print('Viajero: %s Millas: %d'%(objeto.getnumero(), objeto.cantidadTotalMillas()))
                
        for objeto in self.__listaobjetos:
            if valor == objeto:
                print('Viajero: %s Millas: %d'%(objeto.getnumero(), objeto.cantidadTotalMillas()))

    def acumularSobrecargarReverso(self):
        print('\n')
        print('Acumular')
        i = 0
        for objeto1 in self.__listaobjetos:
            i+=1
            print('Viajero (%d)'%i)
            millas = int(input('Ingrese la cantidad de millas recorridas: '))
            objeto1 = millas + objeto1
            print(objeto1.muestra())

    def canjearSobrecargaReverso(self):
        print('\n')
        print('Canjear')
        i = 0
        for objeto in self.__listaobjetos:
            i+=1
            print('Viajero ()',i)
            canje = int(input('Ingrese la cantidad de millas a canjear: '))
            objeto = canje - objeto
            print(objeto.muestra())