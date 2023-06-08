from helado import Helado

class manejadorHelados:
    __listaH: list

    def __init__(self) -> None:
        self.__listaH = []

    def addHelado(self, h):
        self.__listaH.append(h)

    def __str__(self) -> str:
        s = ''
        for helado in self.__listaS:
            s += str(helado)
        return s

    def venta (self, mS):
        g = int (input ('Ingrese cantidad de gramos del helado (100gr, 150 gr, 250 gr, 500 gr y 1000gr): '))
        p = int (input ('Ingrese Precio: '))
        cant = int (input ('Ingrese cantidad de sabores: '))
        print ('elija los sabores:')
        print (str(mS))
        xHelado = Helado (g, p)
        self.addHelado(xHelado)
        j = 1
        for i in range (cant):
            xId = int (input (f'Ingrese id del sabor {j}: '))
            sabor = mS.getSaborPorId(xId-1)
            mS.sumarContador(xId-1)
            xHelado.addSabor(sabor)
            j += 1
        #self.mostrarPedido(xHelado)

    def mostrarPedido (self, xh):
        print(f'''
Pedido: 
gramos: {xh.getGramos()}
sabores:''')
        for sabor in xh.getSabores():
            print (str (sabor))
            print (sabor.getContador())

    def calculoGramos (self, g, cant):
        return g/cant


    def estimarGramos (self, xs):
        r = 0
        for h in self.__listaH:
            for s in h.getSabores():
                if xs == s.getNombreSabor():
                    g = h.getGramos()
                    r += float(self.calculoGramos(g, len(h.getSabores())))
        return r

    def saboresVendidos (self, xh):
        print (f'---------->sabores vendidos en {int(xh)}g <----------')
        aux = ''
        for h in self.__listaH:
            if h.getGramos() == xh:
                for s in h.getSabores():
                    if s != aux:
                        print (f'{s.getNombreSabor()}')
                        aux = s.getNombreSabor()

    def recaudacionTotal(self):
        r = {}
        for h in self.__listaH:
            precio = h.getPrecio()
            gramos = h.getGramos()
            if gramos not in r:
                r[gramos] = precio
            else: r[gramos] += precio
        return r