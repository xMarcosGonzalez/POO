from ManejadrAlumnos import ManejadorAlumnos
from ManejadorMaterias import ManejadorMaterias


if __name__ == '__main__':
    manejadorA = ManejadorAlumnos()
    manejadorM = ManejadorMaterias()
    manejadorM.CargaM()
    nombre = input('Ingrese : ')
    valor = manejadorC.buscarMostrar(nombre)
    manejadorM.mostrar(valor)
    s = input('Ingrese : ')
    manejadorC.listar(s)
