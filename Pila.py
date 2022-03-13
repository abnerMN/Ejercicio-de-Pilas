
class Pila:
    class NodoOrden:
        def __init__(self, nombre,pizza, cantidad, tiempo):
            self.Nombre = nombre
            self.pizza = pizza
            self.cantidad = cantidad
            self.tiempo = tiempo
            self.nodo_siguiente = None
        
        def obtenerInfo(self):
            return ("\nNombre: " + self.Nombre+"\nPizza: " + self.pizza+"\nCantidad: "+ str(self.cantidad)+"\nTiempo: " + str(self.tiempo))

        def datos(self):
            return ("\n*** Orden a Entregar ***"+"\nNombre: " + self.Nombre+"\nPizza: " + self.pizza+"\nCantidad: "+ str(self.cantidad))

    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamaño = 0

    def agregar(self, nombre, pizza, cantidad, tiempo): #inserta el elemento
        tiempo=tiempo*cantidad
        nuevoNodoOrden = self.NodoOrden(nombre,pizza,cantidad,tiempo)
        if self.cabeza == None and self.cola == None:
            self.cabeza = nuevoNodoOrden
            self.cola = nuevoNodoOrden
        else:
            self.cola.nodo_siguiente = nuevoNodoOrden
            self.cola = nuevoNodoOrden
        self.tamaño += 1

    def quitar(self): #saqua el elemento
        if self.tamaño == 0:
            self.cabeza = None
            self.cola = None
        else:
            nodo_eliminado = self.cabeza
            self.cabeza = nodo_eliminado.nodo_siguiente
            nodo_eliminado.nodo_siguiente = None
            self.tamaño -= 1
            return print(nodo_eliminado.datos())

    def obtenerLista(self): #mostar los elementos
        respuesta =''
        nodo_actual = self.cabeza
        while nodo_actual != None:
            respuesta+=nodo_actual.obtenerInfo()+'\n'
            nodo_actual = nodo_actual.nodo_siguiente
        if respuesta=='':
            respuesta=None
        return respuesta 

    def calcularTiempo(self): #calcula el tiempo en cola
        tiempoCola=0
        nodo_actual = self.cabeza
        while nodo_actual != None:
            tiempoCola += nodo_actual.tiempo
            nodo_actual = nodo_actual.nodo_siguiente
        return tiempoCola
