import os

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1: self.opc1,
                            2: self.opc2,
                            3: self.opc3,
                            4: self.opc4,
                            5: self.opc5,
                            0: self.salir
                        }

    def opcion(self,op, mS, mH):
        func=self.__switcher.get(op, lambda: print("Opción no válida, intente de nuevo"))
        if op == 1 or op == 2 or op == 3 or op == 4 or op== 5:
            func(mS, mH)
        else:
            func()

    def mostrarMenu(self):
        print("""
---------->Menu Principal<----------

-> 1: Registrar helado vendido
-> 2: Mostrar 5 sabores de helado más pedidos
-> 3: Estimar el total de gramos vendidos de un sabor
-> 4: Mostrar los sabores vendidos por una cantidad
-> 5: Determinar el importe total recaudado por la Heladería
-> 0: Salir del programa
""")

## OPCIONES

    def opc1 (self, mS,  mH):
        os.system('cls')
        mH.venta(mS)

    def opc2 (self, mS,  mH):
        os.system('cls')
        mejoresSabores = mS.mostrarMejores()
        print ('---------->Mejores Sabores<----------')
        for sabor in mejoresSabores:
            print(f"Sabor: {sabor.getNombreSabor()}, Cantidad vendida: {sabor.getContador()}")

    def opc3 (self, mS,  mH):
        os.system('cls')
        sabor = input ('Ingrese sabor de helado: ')
        r = mH.estimarGramos(sabor)
        print ('se vendieron {:,.2f}g del sabor {}'.format(r, sabor))

    def opc4 (self, mS, mH):
        os.system('cls')
        helado = float (input ('ingrese el tamaño de helado: '))
        mH.saboresVendidos(helado)

    def opc5 (self, mS, mH):
        os.system('cls')
        print("---------->Recaudación por tipo de helado<----------")
        r = mH.recaudacionTotal()
        for gramos, precio in r.items():
            print (f'{gramos}g: ${precio}')


    def salir (self):
        print ('saliendo...')
