class Email():
    __idCuenta = 'idCuenta'
    __Dominio = 'dominio'
    __tipoDominio = 'tipodominio'
    __Contrasenia = 'contrasenia'

    def __init__(self,idCuenta='',Dominio='',tipoDominio='',Contrasenia=''):
        self.__idCuenta=idCuenta
        self.__Dominio=Dominio
        self.__tipoDominio=tipoDominio
        self.__Contrasenia=Contrasenia

    def retornaMail(self):
        print("Retorna Mail")
        emailx=self.__idCuenta+'@'+self.__Dominio+'.'+self.__tipoDominio
        #print('Email creado {}'.format(emailx))
        return(print('Email creado {}'.format(emailx)))

    def getDominio(self):
        print("Obtener dominio")
        dom=self.__idCuenta
        print(dom)

    def CrearCuenta(self, correo):
        print("\n Creando Cuenta")
        correo=correo.split('@')
        self.__idCuenta=correo[0]
        correo=correo[1].split('.')
        self.__Dominio=correo[0]
        self.__tipoDominio=correo[1]

        con = input("Ingrese una clave de acceso -->")
        self.__Contrasenia=con

        """
           def CrearCuenta(self,correo):
                self.__idCuenta=correo.split('@')
                self.__Dominio=correo.split('.')
                self.__tipoDominio=correo
        """

    def ModificarContrasenia(self):
        print("\n Modificar Clave")

        oldPAss = input("Ingrese su anterior clave -->")
        if oldPAss==self.__Contrasenia:
            print("Clave Correcta")
            nPass = input("Ingrese su Nueva clave -->")
            self.__Contrasenia=nPass
            print("Clave Actualizada Correctamente")
        else:
            print("Clave Incorecta")
            print(self.__Contrasenia)