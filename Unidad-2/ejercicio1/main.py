from ClaseEmail import Email
from ManejadorEmail import ListaManejador

if __name__ == '__main__':

    print('Ejercicio 1')

    lista=ListaManejador()
    lista.leerArchivo()

    dom=input("Ingrese dominio a buscar ->")
    lista.buscarDominio(dom)


    correo='alumnopoo@gmail.com'
    cuenta = Email()
    cuenta.CrearCuenta(correo)
    cuenta.retornaMail()
    cuenta.getDominio()

    #correo=input("Ingrese email -->")
    correo='mdg@gmail.es'
    c1=Email()
    c1.CrearCuenta(correo)
    c1.getDominio()
    c1.retornaMail()

    persona = input("Ingrese su nombre -->")
    correo = input("Ingrese email -->")
    c2=Email()
    c2.CrearCuenta(correo)
    print('Estimado {}'.format(persona),'te enviaremos tus mensajes a la direccion {}'.format(correo))
    c2.ModificarContrasenia()

    """ archivo = open('listaemail.csv')
    reader = csv.reader(archivo, delimiter=',')
    cvarias=Email()"""

    """ listaDominio=[]


    for linea in reader:
        #cvarias.CrearCuenta(fila[])
        print("cuenta-> \n",linea[0])
        cvarias.CrearCuenta(linea[0])
        correo=linea[0]
        correo = correo.split('@')
        correo=correo[1].split('.')
        listaDominio.append(correo[0])
        print(listaDominio)
    c=0

    dom=input("Ingrese dominio a buscar ->")
    for i in listaDominio:
        if i==dom:
            c=c+1

    print("La cantidad de cuentas cn el mismo dominio es de:", c)"""