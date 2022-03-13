from Pila import Pila

Pila = Pila()

def agregarOrden ():
    global Pila
    pizzas={'1': 'Pepperoni','2': 'Salchicha','3': 'Carne','4': 'Queso','5': 'Piña'}
    nombre = input("Ingrese nombre del cliente: \n")
    bandera=False
    while(bandera==False):
        print('Seleccione una pizza:\n')
        for pizza in pizzas:
            print(pizza, ". ", pizzas[pizza])
        try:
            sl_piza = int(input())
            if sl_piza >0 and  sl_piza<6:
                try:
                    cantidad = int(input('Ingrese la cantidad a ordenar: \n'))
                    if sl_piza ==1:
                        tiempo= 3
                        Pila.agregar(nombre,pizzas.get(str(sl_piza)),cantidad,tiempo)
                        tmp=Pila.calcularTiempo()
                        print('Tiempo de espera: ' + str(tmp))
                    elif sl_piza ==2:
                        tiempo= 4
                        Pila.agregar(nombre,pizzas.get(str(sl_piza)),cantidad,tiempo)
                        tmp=Pila.calcularTiempo()
                        print('Tiempo de espera: ' + str(tmp))
                    elif sl_piza ==3:
                        tiempo= 10
                        Pila.agregar(nombre,pizzas.get(str(sl_piza)),cantidad,tiempo)
                        tmp=Pila.calcularTiempo()
                        print('Tiempo de espera: ' + str(tmp))
                    elif sl_piza ==4:
                        tiempo= 5
                        Pila.agregar(nombre,pizzas.get(str(sl_piza)),cantidad,tiempo)
                        tmp=Pila.calcularTiempo()
                        print('Tiempo de espera: ' + str(tmp))
                    elif sl_piza ==5:
                        tiempo= 2
                        Pila.agregar(nombre,pizzas.get(str(sl_piza)),cantidad,tiempo)
                        tmp=Pila.calcularTiempo()
                        print('Tiempo de espera: ' + str(tmp))
                    bandera=True
                except:
                    print('*** ERROR: Solo se permite el ingreso de numeros enteros ***')

            else:
                print('*** ERROR: La seleccion tiene que ser entre 1 y 5 ***')
        except:
            print('*** ERROR: Seleccione una opcion correcta ***')

def menu ():
    seleccion= 0
    while (seleccion !=5):

        print ('\n**************************')
        print ('\n          Menu')
        print ('\n**************************')
        print('1. Nueva Orden')
        print('2. Entregar Orden')
        print('3. Imprimir Listado de Ordenes')
        print('4. Datos del Programador')
        print('5. Salir')
        print ('**************************\n')

        try:
            seleccion = int(input('Seleccione una opcion: \n'))
            if seleccion == 1:
                agregarOrden()
            elif seleccion ==2:
                Pila.quitar()
            elif seleccion == 3:
                if Pila.obtenerLista()==None:
                    print('Cola Vacia')
                else:
                    print(Pila.obtenerLista())
            elif seleccion == 4:
                print('Abner Martín Noj Hernández -- 201801027')
            elif seleccion == 5:
                print ("*** Adios ***")
            else:
                print ('*** Opcion no disponible ***')
        except:
            print('*** Por favor seleccione una opcion valida ***')

#main
if  __name__ == '__main__':
    menu()